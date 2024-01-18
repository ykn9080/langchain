from IPython.display import display,Markdown as md,display_markdown
import apikey
apikey.getgoogle()

from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-pro")
result=llm.invoke("네이버에 대해 보고서를 작성해줘")

print(result.content)

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader

loader=PyPDFLoader("data/realestate.pdf")
pages=loader.load_and_split()

text_splitter= RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts=text_splitter.split_documents(pages)



# rag와 결합
from langchain.embeddings import HuggingFaceBgeEmbeddings
model_name="jhgan/ko-sbert-nli"
model_kwargs={'device':'cpu'}
encode_kwargs={'normalize_embeddings':True} 
hf=HuggingFaceBgeEmbeddings(model_name=model_name,model_kwargs=model_kwargs,encode_kwargs=encode_kwargs)

docsearch=Chroma.from_documents(texts,hf)
retriever=docsearch.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3,"fetch_k":10}
retriever.get_relevant_context("2023년 재건축시장 동향은 어떻게 될까요?")


)


from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap

template="""
Answer the question as based only on the following context:
{context}
Question: {question}
"""
prompt=ChatPromptTemplate.from_template(template)

gemini=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0)
chain=RunnableMap({
    "context":lambda x:retriever.get_relevant_context(x["question"]),
    "question":lambda x:x["question"],
}) | prompt | gemini

display_markdown(chain.invoke({'question': "네이버에 대해 보고서를 작성해줘" }).content)