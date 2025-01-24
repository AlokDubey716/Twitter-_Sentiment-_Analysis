import streamlit as st

st.set_page_config(page_title="Text & CSV Analysis App", page_icon="📊", layout="centered")

st.title("📊 Text & CSV Analysis App")
st.write("Welcome to the Text & CSV Analysis App!")

st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar to navigate between pages.")
st.markdown(
    """
    ### Available Features:
    - 📈 Text Sentiment Analysis
    - 🧹 Text Cleaning Tool
    - 📊 CSV Sentiment Analysis
    """
)

st.image("assets/banner.png", use_column_width=True)
st.write("Developed by Your Name")
