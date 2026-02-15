from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])  
def emotion_detector_output():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Request content-type must be application/json"}), 415
        data = request.get_json()
        user_input = data.get('statement', '')
    else: 
        user_input = request.args.get('textToAnalyze', '')

    if not user_input:
        return "Invalid text! Please try again."

    emotions = emotion_detector(user_input)

    dominant_emotion = emotions.pop('dominant_emotion', None)
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    
    emotions_formatted = str(emotions).replace("{", "").replace("}", "")
    emotions_str = (
        f"For the given statement, the system response is {emotions_formatted}. "
        f"The dominant emotion is {dominant_emotion}.")

    return emotions_str

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)