import requests
import json

def emotion_detector(text_to_analyse):
    """
    Analyze sentiment of the given text using Watson NLP API.
    
    Args:
        text_to_analyse (str): Input text to analyze
    
    """
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=input_json, headers=headers)
    
    """  
    output formatting takes place here 

    return:
        {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': '<name of the dominant emotion>' (max_emo)
        }
    """
    #make it JSON
    resp_dict = json.loads(response.text)
    resp_data = resp_dict['emotionPredictions'][0]['emotion']

    #list out all the emotions
    anger_score = resp_data['anger']
    disgust_score = resp_data['disgust']
    fear_score = resp_data['fear']
    joy_score = resp_data['joy']
    sadness_score = resp_data['sadness']

    #returns max value for dominant emotion
    keys = resp_data.keys()
    max_val = max([anger_score, disgust_score, fear_score, sadness_score, joy_score])
    for x in keys:
        if resp_data[x] == max_val:
            max_emo = x #dominant emotion
    
    #returning the dictionary with update for error handling
    if response.status_code == 200:
        return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': max_emo
                }
    elif response.status_code == 400:
        return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': max_emo
                }
    else:
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                }