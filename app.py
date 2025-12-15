import streamlit as st
from logic import generate_explanation

# Page Configuration
st.set_page_config(
    page_title="ELI5 Generator",
    page_icon="🧠",
    layout="centered"
)

# The Title & Header
st.title("🧠 Explain It Like I'm 5")
st.caption("Powered by Groq & LangChain 🚀")


st.markdown("""
**How this works:**
1. **🧐 Technical Explanation** (Standard definition)
2. **🧸 ELI5 Explanation** (Simple analogy & quiz)
""")
# -----------------------

st.divider()

# 3. User Input
topic = st.text_input("Enter a complex topic:", placeholder="e.g. Quantum Computing, Inflation, Photosynthesis")

# The Button Logic
if st.button("Explain It!", type="primary"):
    if not topic:
        st.warning("Please enter a topic first! 🛑")
    else:
        with st.spinner("Thinking... (Consulting Professor Sparkle 🧸)"):
            try:
                result = generate_explanation(topic)
                st.markdown(result)
                st.success("Explanation generated successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# 5. Footer
st.markdown("---")
st.caption("Developed by Kaushik | Powered by Groq & LangChain")