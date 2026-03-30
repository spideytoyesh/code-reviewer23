import streamlit as st
import os
import google.generativeai as genai
import re

# 🔐 Configure API safely
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API key not found. Please set GEMINI_API_KEY in secrets.")
    st.stop()

genai.configure(api_key=api_key)

# 🎯 UI
st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🤖 AI Code Reviewer")
st.write("Analyze your code using AI")

language = st.selectbox(
    "Select Language",
    ["Python", "JavaScript", "C++", "Java"]
)

code = st.text_area("Paste your code here", height=300)

# 🧠 AI function (SAFE)
def review_code_ai(code, language):
    try:
        model = genai.GenerativeModel("gemini-pro")  # stable

        prompt = f"Review this {language} code and give bugs and improvements:\n{code}"

        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text
        else:
            return "No response from AI"

    except Exception as e:
        return f"Error: {str(e)}"

# 🚀 Button
if st.button("Analyze Code"):
    if code.strip() == "":
        st.warning("Please paste code first")
    else:
        st.info("🧠 AI analyzing...")

        result = review_code_ai(code, language)

        st.markdown("### 🧠 AI Review")
        st.write(result)

        st.code(code, language=language.lower())
