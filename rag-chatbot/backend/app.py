# backend/app.py

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


def build_qa_chain():
    # Load saved vector database
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vectorstore", embedding_model)

    retriever = db.as_retriever(search_kwargs={"k": 4})

    # OpenAI LLM
    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Optional: custom prompt to add context boundaries
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "You are a helpful insurance support assistant.\n"
            "Answer the question using only the context provided below.\n"
            "If the answer is not in the context, respond with 'I don't know'.\n\n"
            "Context:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"
        ),
    )

    # Build QA chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa
