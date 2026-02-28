# Import requests to access libraries
import requests
import json

# Defining the function to be used
def emotion_detector(text_to_analyze):
    # URL of the emotion detection service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"  
    # Custom header specifying the model ID for the emotion detection service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    # Constructing the request payload in the expected format 
    payload = {"raw_document": {"text": text_to_analyze}}
    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=payload, headers=headers)
    
    # Parse the response JSON
    response_dict = json.loads(response.text)
    
    # Extract emotion scores from the correct path in the response
    emotion_scores = response_dict['emotionPredictions'][0]['emotion']
    
    # Find the dominant emotion (emotion with highest score)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Format and return the output dictionary
    return {
        'anger': emotion_scores.get('anger', 0),
        'disgust': emotion_scores.get('disgust', 0),
        'fear': emotion_scores.get('fear', 0),
        'joy': emotion_scores.get('joy', 0),
        'sadness': emotion_scores.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }