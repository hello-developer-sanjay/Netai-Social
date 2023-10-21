from flask import Blueprint, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from models.message_model import Message
message_routes = Blueprint('message_routes', __name__)

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

@message_routes.route('/', methods=['GET'])
def home():
    return "Welcome to NetAI Social!"

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
            inputs = tokenizer(text, return_tensors='pt')
            outputs = model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=1)
            sentiment = "POSITIVE" if predictions.item() == 1 else "NEGATIVE"
            
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
            inputs = tokenizer(text, return_tensors='pt')
            outputs = model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=1)
            sentiment = "POSITIVE" if predictions.item() == 1 else "NEGATIVE"
            
            emotion = analyze_emotion(text)
            message = Message(text, sentiment, emotion)
            message.save()
            return jsonify({"message": "Message created successfully!"}), 201
        return jsonify({"error": "Text is required."}), 400
