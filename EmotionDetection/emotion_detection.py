""" Task 3 Format output of emotion detector """

import requests
import json

""" Call Watson NLP service to assess sentiment of text """
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL,
        headers = header,
        json = data )

    # Check if the request was successful
    if response.status_code == 200:
        resp = json.loads(response.text) # Convert text to dict
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    emo_scores = resp["emotionPredictions"][0]["emotion"]
    max_score = 0
    for emo, score in emo_scores.items():
        if score > max_score:
            max_score = score
            predom_emo = emo

    #print(f"Dominant_emotion is: {predom_emo} with score of {max_score}\n\n")
    emo_scores["dominant_emotion"] = predom_emo

    return emo_scores

if (__name__ == '__main__'):
    formatted_text = emotion_detector("I love this new technology")
    print(formatted_text)

