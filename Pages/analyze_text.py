import streamlit as st
from textblob import TextBlob

st.title("📈 Text Sentiment Analysis")
text = st.text_area("Enter text to analyze:")

if st.button("Analyze Sentiment"):
    if text:
        blob = TextBlob(text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write("**Polarity:**", polarity)
        st.write("**Subjectivity:**", subjectivity)

        if polarity > 0:
            st.success("Positive Sentiment 😊")
        elif polarity < 0:
            st.error("Negative Sentiment 😡")
        else:
            st.info("Neutral Sentiment 😐")
    else:
        st.warning("Please enter text to analyze.")
