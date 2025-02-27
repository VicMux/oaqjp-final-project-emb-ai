# Import the Flask class from the flask module
from flask import Flask, make_response, request
from EmotionDetection import emotion_detection as ed 
import requests


# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

@app.route("/emotionDetector")
def emotionDetector():
    statement = request.args.get('q')
    if not statement == request.args.get('q'):
        return {"message" : "Query parameter 'q' is missing"}, 422
    
    resp = ed.emotion_detector(statement)
    
    dominant_emotion = resp['dominant_emotion']
    sys_resp = str(resp).replace('{','').replace('}','')
    sentiment = "For the given statement, the system response is " + sys_resp + ". The dominant emotion is " + dominant_emotion

    return(sentiment)