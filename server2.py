# Import the Flask class from the flask module
from flask import Flask, make_response, request
import requests


# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)