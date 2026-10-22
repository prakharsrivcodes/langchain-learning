
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.header("Research Paper Explainer")

paper_input = st.selectbox("Select Research Paper Name", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"
])

style_input = st.selectbox("Select Explanation Style", [
    "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"
])

length_input = st.selectbox("Select Explanation Length", [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)"
])

if st.button("Summarize"):
    prompt = f"""
    Explain the research paper: {paper_input}.
    Explanation style: {style_input}.
    Explanation length: {length_input}.

    Explain the paper according to the selected style and length.
    """

    result = model.invoke(prompt)
    st.write(result.content)
