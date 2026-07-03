import streamlit as st
from textblob import TextBlob

# Set page configuration
st.set_page_config(page_title="Sentiment Analyzer", page_icon="😊")

def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Polarity is a float within the range [-1.0, 1.0]
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive", "😊"
    elif polarity < 0:
        return "Negative", "😞"
    else:
        return "Neutral", "😐"

# UI Layout
st.title("Sentiment Analysis Tool")
st.write("Enter a sentence below to analyze its sentiment.")

user_input = st.text_area("Input Text", height=150)

if st.button("Analyze"):
    if user_input.strip():
        sentiment, emoji = analyze_sentiment(user_input)
        
        # Display results in columns
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Sentiment", sentiment)
        with col2:
            st.title(emoji)
            
        st.success(f"Polarity Score: {TextBlob(user_input).sentiment.polarity:.2f}")
    else:
        st.warning("Please enter some text to analyze.")