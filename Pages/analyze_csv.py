import streamlit as st
import pandas as pd
from textblob import TextBlob

st.title("📊 CSV Sentiment Analysis")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(df.head())

    if 'tweet' not in df.columns:
        st.warning("The CSV file must contain a column named 'tweet'.")
    else:
        # Perform sentiment analysis
        df['score'] = df['tweet'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        df['analysis'] = df['score'].apply(lambda x: 'Positive' if x >= 0.5 else ('Negative' if x <= -0.5 else 'Neutral'))

        st.write("Analyzed Data:")
        st.write(df[['tweet', 'score', 'analysis']])

        # Download the analyzed data
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Analyzed Data", data=csv_data, file_name="analyzed_sentiment.csv", mime="text/csv")
