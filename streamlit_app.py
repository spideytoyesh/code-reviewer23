import streamlit as st
import google.generativeai as genai
import os
import re

# 🔐 Configure API Key
genai.configure(api_key=os.getenv("AIzaSyDzk1piIb4DAuqBr3Asb4xXRR5O_2B9kgw"))

# 🤖 Load Model
model = genai.GenerativeModel("gemini-1.5-flash")

# 🎯 Page Config
st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🤖 AI Code Reviewer")
st.markdown("""
Analyze your code using AI to detect bugs, improve readability, and optimize performance.
""")

# 🌐 Language selection
language = st.selectbox(
    "Select Programming Language",
    ["Python", "JavaScript", "C++", "Java", "Other"]
)

# 💻 Code input
code = st.text_area("Paste your code here", height=300)

# 🧠 AI Function
def review_code_ai(code, language):
    prompt = f"""
You are a senior software engineer.

Review the following {language} code and provide:

1. Bugs
2. Improvements
3. Readability suggestions
4. Optimization tips
5. Code quality score out of 10
6. Short reason for score

Format:

Score: X/10
Reason: ...

Bugs:
- ...

Improvements:
- ...

Readability:
- ...

Optimization:
- ...

Code:
{code}
"""

    response = model.generate_content(prompt)
    return response.text

# 🚀 Button Action
if st.button("🔍 Analyze Code"):
    if code.strip() == "":
        st.warning("Please paste some code first!")
    else:
        st.info("🧠 AI is analyzing your code...")

        result = review_code_ai(code, language)

        # 📊 Extract Score
        score_match = re.search(r"Score:\s*(\d+)/10", result)

        if score_match:
            score = int(score_match.group(1))

            st.markdown("## 📊 Code Quality Score")
            st.progress(score * 10)
            st.metric("Score", f"{score}/10")

            if score >= 8:
                st.success("Excellent code quality 🚀")
            elif score >= 5:
                st.warning("Decent but needs improvement ⚡")
            else:
                st.error("Poor quality code ❌")

        # 🧠 AI Output
        st.markdown("### 🧠 AI Review")
        st.write(result)

        # 💻 Show Code
        st.markdown("### 💻 Your Code")
        st.code(code, language=language.lower())

        st.divider()

# 📌 Footer
st.caption("Built using Streamlit + Google Gemini AI")
