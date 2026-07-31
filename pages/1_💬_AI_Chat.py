import streamlit as st

st.set_page_config(page_title="AI Chat", page_icon="💬")

st.title("💬 AI Healthcare Chat")

st.write("Ask your healthcare or biomedical engineering questions below.")

question = st.text_area("Enter your question")

if st.button("Ask AI"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        st.success("AI response will appear here.")
