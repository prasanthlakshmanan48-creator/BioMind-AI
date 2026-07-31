import streamlit as st
import google.generativeai as genai

# ----------------- Configure Gemini -----------------

API_KEY = "AQ.Ab8RN6LdclW51W8PIJ3knQr-lyfeIYqNcPDkbgHWEZ7QHjgEIQ"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------- Page -----------------

st.set_page_config(page_title="AI Chat", page_icon="💬")

st.title("💬 BioMind AI Chat")

st.write("Ask any healthcare or biomedical engineering question.")

question = st.text_area("Enter your question")

if st.button("Ask AI"):

    if question == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            response = model.generate_content(question)

            st.success("Answer")

            st.write(response.text)
