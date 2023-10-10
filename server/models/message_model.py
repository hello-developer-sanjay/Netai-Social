from config.db_config import db

class Message:
    def __init__(self, text, sentiment, emotion):
        self.text = text
        self.sentiment = sentiment
        self.emotion = emotion

    def save(self):
        messages_collection = db.messages
        messages_collection.insert_one({
            "text": self.text,
            "sentiment": self.sentiment,
            "emotion": self.emotion
        })

    @staticmethod
    def get_all_messages():
        messages_collection = db.messages
        messages = list(messages_collection.find({}, {"_id": 0}))
        return messages
