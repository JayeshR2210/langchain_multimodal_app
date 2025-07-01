# 🧠 LangChain Multi-Model Streamlit App

This project is a demonstration of how to use multiple **LangChain chains** with different LLMs (OpenAI + Hugging Face) in a unified **Streamlit UI**. It showcases:

- 🔁 **Parallel Chain**: Generate Product Insights (Summary, Audience, Tagline) using 3 LLMs.
- ⚖️ **Conditional Chain**: Career guidance based on whether the query is tech or non-tech.

---

## 🚀 Features

### 🔍 Product Insights Generator (Parallel Chain)
- Uses 3 different LLMs in parallel.
- Generates:
  - One-line product summary
  - Potential audience
  - Creative tagline
- Merges them into a single paragraph.

### 💼 Career Advice Bot (Conditional Chain)
- Classifies query into:
  - Tech-related
  - Other career-related
- Gives targeted advice based on the classification.
