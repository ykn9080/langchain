from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Pinecone
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
import pinecone
import apikey
import api


model_name="jhgan/ko-sbert-nli"
model_kwargs={'device':'cpu'}
encode_kwargs={'normalize_embeddings':True} 
hf=HuggingFaceEmbeddings(model_name=model_name,model_kwargs=model_kwargs,encode_kwargs=encode_kwargs)


def createDB():
    loader=PyPDFLoader("data/realestate.pdf")
    pages=loader.load_and_split()

    # print(pages)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs=text_splitter.split_documents(pages)
    pinecone.init(
        api_key=apikey.getpinecone(),
        environment="gcp-starter"
    )
    index_name="yknam-sample"
    index=Pinecone.from_documents(docs,hf,index_name=index_name)
    
def findDB():
    pinecone.init(
        api_key=apikey.getpinecone(),
        environment="gcp-starter"
    )
    index_name="yknam-sample"
    index = Pinecone.from_existing_index(index_name, hf)
    index=api.api_vectorStores.getdb("pinecone", index_name,hf)
    return index
def main():
    db3=api.api_vectorStores.getdb("pinecone", "yknam-sample",hf)
    query="2023년 재건축시장 동향은 어떻게 될까요?"

    docs=db3.similarity_search(query)
    print("question:{} \n".format(query))
    print(docs)
    # for i in range(len(docs)):
    #     print("{0}번째 유사문서 유사도 \m{1}".format(i+1, round(docs[i][1],2)))
    #     print("-"*100)
    #     print(docs[i][0].page_content)
    #     print("\n")
    #     print(docs[i][0].metadata)
    #     print("-"*100)
def maxMargin():
    # 반환값이 서로 상이하게 다양한 결과를 만들어냄 
    db3=api.api_vectorStores.getdb("pinecone", "yknam-sample",hf)
    query="2023년 재건축시장 동향은 어떻게 될까요?"

    docs=db3.max_marginal_relevance_search(query, k=3,fetch_k=10,lambda_mult=0.5)
    #10개의 문서를 상위 3개의 문서로 줄임, lambda_mult는 0~1 다양성~유사도설정
    
    print("question:{} \n".format(query))
    print(docs)
    # for i in range(len(docs)):
    #     print("{}번째 유사문서".format(i+1))
    #     print("-"*100)
    #     print(docs[i].page_content)
    #     print("\n")
    #     print(docs[i].metadata)
    #     print("-"*100)

if __name__ == "__main__":
    maxMargin()


