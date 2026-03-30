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
