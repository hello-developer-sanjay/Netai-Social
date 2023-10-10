from transformers import pipeline

emotion_classifier = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    result = emotion_classifier(text)
    return result[0]['label']

def analyze_emotion(text):
    result = emotion_classifier(text)
    return result[0]['label']
