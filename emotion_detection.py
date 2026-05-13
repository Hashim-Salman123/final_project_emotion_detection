import requests
import json


def emotion_detector(text_to_analyze):
    # Watson NLP API URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # API ke liye headers
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input data (Payload)
    myobj = {"raw_document": {"text": text_to_analyze}}

    # POST request bhejna
    response = requests.post(url, json=myobj, headers=header)

    # Agar response sahi (200) hai toh data nikalna
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']

        # Sabse badi emotion (Dominant Emotion) nikalna
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    # Agar text khali ho ya error aaye (Status 400)
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        return "Error in processing"

# Testing ke liye (optional):
# print(emotion_detector("I love this project!"))