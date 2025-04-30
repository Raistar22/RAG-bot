import streamlit as st
from backend.app import build_qa_chain

st.title("📋 RAG Chatbot for Insurance & Angel One Support")
qa_chain = build_qa_chain()

query = st.text_input("Ask a question based on the insurance PDFs or Angel One Support:")
if query:
    result = qa_chain(query)
    answer = result['result'].strip()
    if "I don't know" in answer or len(answer) < 10:
        st.warning("I don't know")
    else:
        st.success(answer)
