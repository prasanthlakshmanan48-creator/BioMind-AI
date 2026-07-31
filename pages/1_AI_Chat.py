import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Chat", page_icon="💬")

# Configure Gemini
genai.configure(api_key=st.secrets["AQ.Ab8RN6LC1NE2t4xqZIRy2DmRiBDooTV7Rp5LPtMDeE6_QkHhEg"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("💬 BioMind AI Chat")

question = st.text_area("Ask a healthcare or biomedical engineering question")

if st.button("Ask AI"):
    if question.strip():
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(question)
                st.success("Answer")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
