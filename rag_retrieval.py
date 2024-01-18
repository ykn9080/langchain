import api
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

api.apikey.getOpenai()

pages=api.api_document.pdf_loader("data/realestate.pdf")
texts=api.api_textsplit.recursivesplit(pages,500,50,api.api_misc.tiktoken_len)
hf=api.api_embedding.getkosbertnli()
docsearch=api.api_vectorStores.setdb("chroma",texts,hf, "data/chroma_db")

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
openai=ChatOpenAI(model_name="gpt-3.5-turbo",
                  streaming=True, callbacks=[StreamingStdOutCallbackHandler()],
                  temperature=0)

qa=RetrievalQA.from_chain_type(llm=openai,
                               chain_type="stuff",
                               retriever =docsearch.as_retriever(
                                   search_type="mmr",
                                   search_kwargs={"k":3,"fetch_k":10}),
                                return_source_documents=True)
query="수도권 아파트 미분양 추이에 대해 말해줘?"
result=qa(query)
result