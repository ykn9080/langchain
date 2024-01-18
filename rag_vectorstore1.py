import api
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import PyPDFLoader

# loader=PyPDFLoader("data/realestate.pdf")
# pages=loader.load_and_split()

# print(pages)
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0, length_function=api.api_misc.tiktoken_len)
# docs=text_splitter.split_documents(pages)
pages=api.api_document.pdf_loader("data/realestate.pdf")
docs=api.api_textsplit.recursivesplit(pages,1000,0,api.api_misc.tiktoken_len)
#print(docs)


embedding=api.api_embedding.getkosbertnli()
db3=api.api_vectorStores.getdb("chroma","data/chroma_db",embedding)

query="2023년 재건축시장 동향은 어떻게 될까요?"
# docs=db3.similarity_search(query, k=5)

docs=db3.similarity_search_with_relevance_scores(query, k=5)
print(docs[0][0].page_content)
print(docs[0][1])