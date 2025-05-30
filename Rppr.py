from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# Page configuration
st.set_page_config(page_title="AI Research Summarizer", layout="centered")

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

st.title("📚 AI Research Paper Summarizer")
st.markdown("Use AI to get summaries of groundbreaking research papers in your preferred style and length.")

with st.container():
    st.markdown("### 📝 Enter Research Paper Details")

    paper_input = st.text_input("🔍 Research Paper Title", placeholder="e.g. Attention Is All You Need")

    col1, col2 = st.columns(2)

    with col1:
        style_input = st.selectbox("🎓 Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

    with col2:
        length_input = st.selectbox("📏 Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt('Researchpaper/template.json')

if st.button('🔎 Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.markdown("### 🧠 Summary Output")
    st.write(result.content)