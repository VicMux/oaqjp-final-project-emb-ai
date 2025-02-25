import requests

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL,
        headers = header,
        json = data )

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response content
        print("Response status: OK")
        print("Response content:")
        print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")

if (__name__ == '__main__'):
    emotion_detector("I am so happy today")

