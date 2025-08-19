from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text: str):
    """Return sentiment label and confidence score."""
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

# Quick test
if __name__ == "__main__":
    text = "I love sunny days!"
    print(get_sentiment(text))
