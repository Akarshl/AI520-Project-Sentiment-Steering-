import streamlit as st
import pandas as pd
from models.text_generator import generate_text
from models.sentiment_classifier import get_sentiment

# Load sample prompts if available
try:
    sample_prompts = pd.read_csv("data/sample_prompts.csv")
except FileNotFoundError:
    sample_prompts = pd.DataFrame(columns=["prompt", "emotion"])

st.title("Sentiment-Controlled Story Generator")

# Choose between manual input or sample prompts
mode = st.radio("Select input mode:", ["Manual Prompt", "Sample Prompt"])

if mode == "Sample Prompt" and not sample_prompts.empty:
    selected_row = st.selectbox("Choose a sample prompt:",
                                sample_prompts.index,
                                format_func=lambda idx: f"{sample_prompts.iloc[idx]['prompt']} ({sample_prompts.iloc[idx]['emotion']})")
    prompt = sample_prompts.iloc[selected_row]['prompt']
    emotion = sample_prompts.iloc[selected_row]['emotion']
else:
    emotion = st.selectbox("Choose Emotion", ["Happy", "Sad", "Hopeful", "Eerie"])
    prompt = st.text_area("Story Prompt", "Once upon a time...")

if st.button("Generate Story"):
    full_prompt = f"Write a short story in a {emotion.lower()} tone:\n{prompt}\n"
    story = generate_text(full_prompt)
    sentiment, score = get_sentiment(story)
    
    st.subheader("Generated Story")
    st.write(story)
    
    st.subheader("Detected Sentiment")
    st.write(f"{sentiment} ({score:.2f})")
