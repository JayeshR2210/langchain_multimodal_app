import streamlit as st
from chains.prod_insights_generator import final_chain as product_chain
from chains.career_advice_bot import chain as career_chain
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="LangChain Project", layout="centered")
st.title("🧠 LangChain Multi-Model App")

tab1, tab2 = st.tabs(["🔍 Product Insights", "💼 Career Advice"])

# ---------------- Product Insights Tab ----------------
with tab1:
    st.header("Get Product Summary, Audience & Tagline")
    product = st.text_input("Enter a product name:", placeholder="e.g. AirPods Pro")

    if st.button("Generate Insights"):
        with st.spinner("Generating insights..."):
            response = product_chain.invoke({"product": product})
            st.success(response)

# ---------------- Career Advice Tab ----------------
with tab2:
    st.header("Ask a Career Question")
    question = st.text_area("Type your question:", placeholder="e.g. How to get into tech in 2025?")

    if st.button("Get Guidance"):
        with st.spinner("Generating guidance..."):
            result = career_chain.invoke({"text": question})
            st.success(result)