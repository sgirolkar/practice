# Import the Flask module
from flask import Flask, request, make_response

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the API endpoint
@app.route("/status/<int:code>")
def status(code):
    # Create a response object with the requested status code
    response = make_response(f"You requested status code {code}", code)
    # Return the response object
    return response

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
