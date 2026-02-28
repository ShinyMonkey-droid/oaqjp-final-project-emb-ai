from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def analyze_emotion():
    # IMPORTANT: Must match the JavaScript parameter name
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detection function
    result = emotion_detector(text_to_analyze)

    # Format output (IBM grading format)
    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)