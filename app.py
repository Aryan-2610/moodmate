from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

sentiment_model = pipeline("sentiment-analysis")

mood_playlists = {
    "Happy": "https://open.spotify.com/embed/track/39LLxExYz6ewLAcYrzQQyP?utm_source=generator&autoplay=1",
    "Sad": "https://open.spotify.com/embed/track/6frz0CJsV056mPCWkMKCTh?utm_source=generator&autoplay=1",
    "Neutral": "https://open.spotify.com/embed/track/39LLxExYz6ewLAcYrzQQyP?utm_source=generator&autoplay=1"
}

mood_quotes = {
    "Happy": [
        "Happiness is contagious. Share it!",
        "Keep smiling and the world will smile with you."
    ],
    "Sad": [
        "Every storm runs out of rain.",
        "Keep going, better days are coming."
    ],
    "Neutral": [
        "Take a deep breath and enjoy the moment.",
        "Focus on what you can control today."
    ]
}

# Store mood history with text
mood_history = []

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"error": "Empty input"}), 400

    result = sentiment_model(text)[0]
    label = result['label']

    if label == "POSITIVE":
        mood = "Happy"
    elif label == "NEGATIVE":
        mood = "Sad"
    else:
        mood = "Neutral"

    playlist_url = mood_playlists[mood]
    quote = random.choice(mood_quotes[mood])

    # Add to history including user text
    mood_history.append({
        "mood": mood,
        "quote": quote,
        "text": text,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    return jsonify({
        "mood": mood,
        "playlist": playlist_url,
        "quote": quote,
        "confidence": round(result['score'], 2),
        "history": mood_history[-10:]  # last 10 entries
    })

if __name__ == "__main__":
    app.run(debug=True)
