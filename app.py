import streamlit as st

# ------------------ Page Configuration ------------------
st.set_page_config(
    page_title="BioMind AI",
    page_icon="🩺",
    layout="wide"
)

# ------------------ Logo ------------------
try:
    st.image("assets/logo.png", width=120)
except:
    pass

# ------------------ Title ------------------
st.title("🧠 BioMind AI")
st.subheader("Your AI Assistant for Medical Reports, Symptoms & Biomedical Learning")

st.markdown("---")

# ------------------ Welcome ------------------
st.write("""
Welcome to **BioMind AI**.

This application helps you:

- 💬 Chat with an AI Healthcare Assistant
- 📄 Analyze Medical Reports
- 🤒 Check Symptoms
- 🩸 View Healthy Laboratory Ranges
- 🎓 Learn Biomedical Engineering Topics
- ℹ️ Know More About the Application

Use the **sidebar** to navigate through different pages.
""")

st.markdown("---")

# ------------------ Quick Info ------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.info("💬 AI Chat")

with col2:
    st.success("📄 Report Analyzer")

with col3:
    st.warning("🤒 Symptom Checker")

col4, col5, col6 = st.columns(3)

with col4:
    st.info("🩸 Health Parameters")

with col5:
    st.success("🎓 Biomedical Learning")

with col6:
    st.warning("ℹ️ About")

st.markdown("---")

st.caption("© 2026 BioMind AI | Developed by Prasanth L")
