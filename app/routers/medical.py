from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain.chains import RetrievalQA
from app.routers.search.search_router import search2

from app.configurations.config import settings

load_dotenv()

router = APIRouter(
    prefix="/medical",
    tags=["Medical"]
)


OPENAI_API_KEY = settings.openai_api_key
PINECONE_API_KEY = settings.pinecone_api_key


model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
parser = StrOutputParser()

template = """
Answer the question based on the context below. If you can't 
answer the question, reply ONLY "I don't know".

Context: {context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)


loader = TextLoader(r"C:\Users\rickb\OneDrive\Desktop\Projects\mr2\app\routers\clinicss.txt")
text_documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
documents = text_splitter.split_documents(text_documents)


embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
pinecone = PineconeVectorStore.from_documents(
    documents, embeddings, index_name="clinics"
)


@router.post("/query")
def query_medical(condition: str):
    try:
        query = f"Which clinic offers {condition}?"
        retriever = pinecone.as_retriever()
        qa = RetrievalQA.from_chain_type(
            llm=model,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
        )
        result = qa({"query": query})
        return {"result": result["result"]}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/query2")
def query_upgraded(condition: str):
    try:
        query = f"Which clinic offers {condition}?"
        retriever = pinecone.as_retriever()
        qa = RetrievalQA.from_chain_type(
            llm=model,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )
        result = qa({"query": query})
        if result["result"] == "I don't know":
            search_result = search2({"query": f"Which clinic in Los Angeles offers treatments for {condition}? What days are they open and where are they located"})
            return search_result
        return {"result": result["result"]}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))