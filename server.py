"""
This module initiates the Flask application for the Emotion Detection project.
It provides routes for rendering the index page and processing emotion 
analysis requests.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    """
    Renders the main index page of the application.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_analyzer():
    """
    Analyzes the text provided by the user for emotional content 
    and returns a formatted response.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    