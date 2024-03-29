from requests import Request, Session, utils as req_utils
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from shlex import quote
from requests.exceptions import RequestException

import urllib3
import logging


LOG = logging.getLogger("root")

class LogRetry(Retry):
    """Adding extra logs before making a retry request"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.history and not self.is_exhausted():
            LOG.info(f"Retry Attempt {len(self.history)}")


class CustomSession(Session):
    """
    A custom Session class with simplified methods and special logging
    """

    def __init__(self):
        """
        Initialize: Set retry strategy
        """
        super().__init__()
        max_retries = 4
        retry_on = frozenset(sorted({408, 502, 500, 503, 504, 413, 429}))
        methods = frozenset(["HEAD", "GET", "POST"])
        backoff = 0.25
        urllib3_version = int(urllib3.__version__.replace(".", ""))
        if urllib3_version > 12510:
            # Do not raiseOnStatus here in retry, 
            # if you do so there will a MaxRetryError which does not have Response object
            # do nt rais on status - print the response and other details in the call 
            # and then in the end raise on status
            retry_strategy = LogRetry(connect=max_retries, read=max_retries, status=max_retries,
                                   status_forcelist=retry_on, allowed_methods=methods,
                                   backoff_factor=backoff)
        else:
            retry_strategy = LogRetry(connect=max_retries, read=max_retries, status=max_retries,
                                   status_forcelist=retry_on,
                                   method_whitelist=methods, backoff_factor=backoff)

        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.mount("https://", adapter)
        self.mount("http://", adapter)

    # This was taken from stackOverFlow. 
    # Sorry I forgot to capture the link. 
    # Most likely was a copy of https://github.com/ofw/curlify/tree/master
    @staticmethod
    def log_curl(req, compressed=False, verify=True):
        """
        Returns string with curl command by provided request object
        Parameters
        ----------
        req: prepared_request
        compressed : bool
            If `True` then `--compressed` argument will be added to result
        verify: bool
            if `True` then `--insecure` argument will be added to result
        """
        parts = [
            ("curl", None),
            ("-X", req.method),
        ]

        for key, val in sorted(req.headers.items()):
            if key.lower() not in ["content-length", "user-agent"]:
                parts += [("-H", f"{key}: {val}")]

        body = getattr(req, "body", None)
        if body:
            if isinstance(body, bytes):
                body = body.decode("utf-8")
            parts += [("-d", body)]

        if compressed:
            parts += [("--compressed", None)]

        if not verify:
            parts += [("--insecure", None)]

        parts += [(None, req.url)]

        flat_parts = []
        for key, val in parts:
            if key:
                flat_parts.append(quote(key))
            if val:
                flat_parts.append(quote(val))
        curl_cmd = " ".join(flat_parts)
        LOG.info(f"Request Curl:\n\n{curl_cmd}")
        return curl_cmd
    
    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)
        print(f"Attempt {len(response.history) + 1}")
        return response

    def call(self, method, url, **kwargs):
        """
        Make a HTTP GET request
        :param method:
        :param url:
        :param kwargs:
        :return:
        """
        if "timeout" not in kwargs:
            kwargs["timeout"] = (2, 5)

        if kwargs.get("is_main_test_call", False):
            LOG.info("\n\n**************************** "
                     "THE MAIN API CALL FROM THE TEST "
                     "***********************************\n\n")

        if "purpose" in kwargs:
            LOG.info(f"Purpose of the request: {kwargs['purpose']}")

        comp = kwargs.get("compressed", False)
        ver =  kwargs.get("verify", False)
        req = Request(
            url=url,
            method=method,
            headers=kwargs.get("headers", None),
            files=kwargs.get("files", None),
            data=kwargs.get("data", None),
            params=kwargs.get("params", None),
            auth=kwargs.get("auth", None),
            cookies=kwargs.get("cookies", None),
            hooks=kwargs.get("hooks", None),
            json=kwargs.get("json", None),
        )
        prep = self.prepare_request(req)
        curl_cmd = self.log_curl(req=prep, compressed=comp, verify=ver)
        response = None
        try:
            response = self.send(
                prep,
                verify=kwargs.get("verify"),
                proxies=kwargs.get("proxies"),
                cert=kwargs.get("cert"),
                timeout=kwargs.get("timeout"),
                allow_redirects=kwargs.get("allow_redirects", True),
                stream=kwargs.get("stream", False),
            )

            LOG.info(f"\n\nRetry Count: {response.history}\n\n")

            LOG.info("Response Status: " + str(response.status_code))
            if response.status_code != 200:
                print("\n\nGot a non 200 response for the following request.\n")
                print(f"{curl_cmd}\n")
                print("Response Status: " + str(response.status_code))
            if response.text:
                # log.info("Response Time: " + str(response.elapsed.total_seconds()) + " seconds")
                LOG.info("Response Headers:  " + str(response.headers))
                LOG.info("Response Body:\n" + response.text.replace("\n", " "))
                if response.status_code != 200:
                    print("Response Headers:  " + str(response.headers))
                    print("Response Body:\n{0}\n\n".format(response.text.replace("\n", " ")))
            if kwargs.get("is_main_test_call", False):
                LOG.info("\n\n**************************** "
                        "END OF THE MAIN API CALL FROM THE TEST "
                        "****************************\n\n")
            # raise exception for error status codes
            response.raise_for_status()
        except RequestException as req_ex:
            print(req_ex)
            # drop the long stack traces
            raise req_ex from None

        return response

    def get(self, url, **kwargs):
        """
        Make a HTTP GET request
        :param url:
        :param kwargs:
        :return:
        """
        return self.call("GET", url, **kwargs)

    def head(self, url, **kwargs):
        """
        Make an HTTP HEAD request
        :param url:
        :param kwargs:
        :return:
        """
        return self.call("HEAD", url, **kwargs)

    def post(self, url, **kwargs):
        """
        Make a HTTP POST request
        :param url:
        :param kwargs:
        :return:
        """
        return self.call("POST", url, **kwargs)

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")

session = CustomSession()
response = session.get("https://httpbin.org/status/500", purpose="Test retry policy", verify=True)