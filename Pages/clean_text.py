import streamlit as st
import cleantext

st.title("🧹 Text Cleaning Tool")
pre = st.text_area("Enter text to clean:")

if st.button("Clean Text"):
    if pre:
        cleaned_text = cleantext.clean(
            pre,
            clean_all=False,
            extra_spaces=True,
            stopwords=True,
            lowercase=True,
            numbers=True,
            punct=True,
        )
        st.write("**Cleaned Text:**")
        st.text_area(label="", value=cleaned_text, height=200)
    else:
        st.warning("Please enter text to clean.")
