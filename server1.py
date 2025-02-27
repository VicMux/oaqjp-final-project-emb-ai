from flask import Flask, make_response, request
from EmotionDetection import emotion_detection as ed 

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    statement = request.args.get('q')
    if not statement == request.args.get('q'):
        return {"message" : "Query parameter 'q' is missing"}, 422

    resp = ed.emotion_detector(statement)
    dominant_emotion = resp['dominant_emotion']

    sentiment = "For the given statement, the system response is " + resp + " The dominant emotion is " + dominant_emotion
    return {"message" : sentiment}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
