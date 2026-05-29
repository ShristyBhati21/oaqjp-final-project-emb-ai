""" 
   Emotion detection server module
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/")
def index_routing():
    """ 
    This is for the HTML routing
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """ 
    This will detect the emotion provided by the user
    """
    text_to_analyze =request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.get("dominant_emotion")
    if dominant_emotion is None :
        return "Invalid text! Please try again!."
    result = " ,".join(f"'{key}' : {value}" for key, value in response.items())
    return (f"For the given statement, the system response is  {result}. "
            f"The dominant emotion is <b>{dominant_emotion}</b>.")

if __name__ == "__main__":
    app.run(debug=True)
