import logging
from config import getOpenai
from langchain_openai import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# load blog post
loader = WebBaseLoader(
    "https://n.news.naver.com/mnews/article/003/0012317114?sid=105")
data = loader.load()

# split blog post into sentences
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=0)
splits = text_splitter.split_documents(data)

# vectordb
model_name = "jhgan/ko-sbert-nli"
encode_kwargs = {"normalize_embeddings": True}
ko_embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    encode_kwargs=encode_kwargs
)


vectordb = Chroma.from_documents(documents=splits, embedding=ko_embedding)

# retriever

getOpenai()

question = "삼성전자 갤럭시 s24는 어떨까?"
llm = ChatOpenAI(temperature=0)
retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=vectordb.as_retriever(),
    llm=llm,
)

# logging

logging.basicConfig(level=logging.INFO)
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

unique_docs = retriever_from_llm.get_relevant_documents(
    query=question)
print(unique_docs)
