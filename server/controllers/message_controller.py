from models.message_model import Message
from utils.ai_utils import analyze_sentiment

def create_message(text):
    sentiment = analyze_sentiment(text)
    message = Message(text, sentiment)
    message.save()
    return message
