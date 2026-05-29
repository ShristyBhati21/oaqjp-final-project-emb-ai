import requests, json
def emotion_detector(text_to_analyze):
    API_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(API_URL, json = payload, headers=headers)
    formated_response = json.loads(response.text)
    emotion_predictions = formated_response['emotionPredictions'][0]
    emotions = emotion_predictions['emotion']
    dominant_emotion = ""
    score = 0
    for emotion in emotions:
       if emotions[emotion] > score:
        dominant_emotion = emotion
        score = emotions[emotion]
    emotions["dominant_emotion"] = dominant_emotion
    return emotions