from collections import deque

S = "bjfgijertnlfoddakfujnybbbbbjfgtgvrvvdecswsxqazwsxedcrfvtgbyhnu" \
    "jmikolpqwertyuioplkjhgfdsazxcvbnmlokmijnuhbygvtfcrdxeszwaqzwsxedcrfvtgbyhnu" \
    "jmikolpqwertyuioplkjhgfds"
CUR_IND = -1


def get_next_char():
    global S, CUR_IND
    CUR_IND += 1
    if CUR_IND < len(S):
        return S[CUR_IND]
    else:
        return None


def search_substring(substring):
    matched = deque()
    next_ch = get_next_char()
    matched.append(next_ch)
    while next_ch is not None:
        sub_ind = 0
        matched_ind = 0

        while sub_ind < len(substring):
            if matched_ind == len(matched):
                next_ch = get_next_char()
                matched.append(next_ch)
            print(matched)
            if substring[sub_ind] == matched[matched_ind]:
                sub_ind += 1
                matched_ind += 1
            else:
                matched.popleft()
                break

        if len(substring) == len(matched):
            print(matched)
            print("Substring found")
            break
    if len(substring) != len(matched):
        print("Substring not found")


substring = "zwsxedcrfvtgbyhnu" \
    "jmikolpqwertyuioplkjhgfdsazxcvbnmlokmijnuhbygvtfcrdxeszwaqzwaq"
search_substring(substring)
