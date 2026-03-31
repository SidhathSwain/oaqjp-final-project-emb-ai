from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_detector():

    #the data is analyzed
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    #mood describe
    anger=response['anger']
    disgust=response['disgust']
    fear=response['fear']
    joy=response['joy']
    sadness=response['sadness']
    dom_emo=response['dominant_emotion']

    #the statement is returned with error handling
    if dom_emo is None:
        return "Invalid text! Please try again!"
    else:
        return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger,disgust,fear,joy,sadness,dom_emo)


@app.route("/") 
def render_index_page(): 
    return render_template('index.html')


if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5500)