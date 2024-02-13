from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import sys
sys.path.append("/home/yknam/ipykernel")
from config import getOpenai, api
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.load.dump import dumps
import streamlit as st

getOpenai()

def main():
    pages = api.api_document.pdf_loader("data/realestate.pdf")
    texts = api.api_textsplit.recursivesplit(
        pages, 500, 50, api.api_misc.tiktoken_len)
    hf = api.api_embedding.getkosbertnli()
    docsearch = api.api_vectorStores.setdb("chroma", texts, hf, "data/chroma_db")

    openai = ChatOpenAI(model_name="gpt-3.5-turbo",
                        streaming=True, callbacks=[StreamingStdOutCallbackHandler()],
                        temperature=0)

    qa = RetrievalQA.from_chain_type(llm=openai,
                                    chain_type="stuff",
                                    verbose=False,
                                    retriever=docsearch.as_retriever(
                                        search_type="mmr",
                                        search_kwargs={"k": 3, "fetch_k": 10}),
                                    return_source_documents=True)
    query = "수도권 아파트 미분양 추이에 대해 말해줘?"

    result = qa({"query": query})
    # print(result['source_documents'][0].metadata['source'],
    #       result['source_documents'][0].metadata['page'])

    st.write(result)
if __name__ == "__main__":
    main()
