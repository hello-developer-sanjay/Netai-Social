from flask import Blueprint, request, jsonify
from utils.ai_utils import analyze_sentiment, analyze_emotion

from models.message_model import Message


message_routes = Blueprint('message_routes', __name__)

@message_routes.route('/', methods=['GET'])
def home():
    return "Welcome to NetAI Social!"
# message_routes.py
@message_routes.route('/api/messages', methods=['GET', 'POST'])
def create_message_route():
    if request.method == 'GET':
        # Handle GET request to retrieve messages
        messages = Message.get_all_messages()
        return jsonify(messages), 200
    elif request.method == 'POST':
        data = request.get_json()
        text = data.get('text')
        aspects = data.get('aspects')  # List of aspects to analyze
        if text and aspects:
            sentiment = analyze_sentiment(text)
            emotions = {aspect: analyze_emotion(f"{aspect} {text}") for aspect in aspects}
            message = Message(text, sentiment, emotions)
            message.save()
            return jsonify({"message": "Message created successfully!"}), 201
        return jsonify({"error": "Text and aspects are required."}), 400

    if request.method == 'GET':
        # Handle GET request to retrieve messages
        messages = Message.get_all_messages()
        return jsonify(messages), 200
    elif request.method == 'POST':
        # Handle POST request to create a new message
        data = request.get_json()
        text = data.get('text')
        if text:
            sentiment = analyze_sentiment(text)
            emotion = analyze_emotion(text)
            message = Message(text, sentiment, emotion)
            message.save()
            return jsonify({"message": "Message created successfully!"}), 201
        return jsonify({"error": "Text is required."}), 400
