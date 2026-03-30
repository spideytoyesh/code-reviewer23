import streamlit as st

st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖")

st.title("🤖 AI Code Reviewer")
st.write("Paste your code below and get feedback instantly!")

code = st.text_area("Paste your code here:")

if st.button("Analyze Code"):
    if code.strip() == "":
        st.warning("Please paste some code first!")
    else:
        st.subheader("AI Review")

        # Simple logic (no API needed)
        if "print" not in code:
            st.write("**Bugs:**\n- Missing print statement")
        else:
            st.write("**Bugs:**\n- No major issues found")

        st.write("**Improvements:**\n- Improve formatting and readability")
        st.write("**Optimization:**\n- Use better structure and naming")
        # 🎯 Simple scoring logic
score = 10

if "print" not in code:
    score -= 2
if len(code) < 20:
    score -= 2
if "for" in code and "range" in code:
    score -= 1

st.markdown("## 📊 Code Quality Score")
st.progress(score * 10)
st.metric("Score", f"{score}/10")

# Feedback based on score
if score >= 8:
    st.success("Excellent code quality 🚀")
elif score >= 5:
    st.warning("Decent but needs improvement ⚡")
else:
    st.error("Poor quality code ❌")
    
bugs = "- Missing print statement" if "print" not in code else "- No major issues"
improvements = "- Improve formatting and readability"

