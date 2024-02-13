from config import api


hf = api.api_embedding.getkosbertnli()


def createDB():

    pages = api.api_document.pdf_loader("data/realestate.pdf")
    docs = api.api_textsplit.recursivesplit(
        pages, 1000, 0, api.api_misc.tiktoken_len)
    api.api_vectorStores.setdb("faiss", docs, hf, "data/faiss_db")


def main():
    # db3=FAISS.load_local("data/faiss_db",hf)
    db3 = api.api_vectorStores.getfaissdb("data/faiss_db", hf)
    query = "2023년 재건축시장 동향은 어떻게 될까요?"

    docs = db3.similarity_search_with_relevance_scores(query, k=5)
    print("question:{} \n".format(query))
    for i in range(len(docs)):
        print("{0}번째 유사문서 유사도 \m{1}".format(i+1, round(docs[i][1], 2)))
        print("-"*100)
        print(docs[i][0].page_content)
        print("\n")
        print(docs[i][0].metadata)
        print("-"*100)


def maxMargin():
    # 반환값이 서로 상이하게 다양한 결과를 만들어냄
    # db3=FAISS.load_local("data/faiss_db",hf)
    # db3 = api.api_vectorStores.getdb("faiss", "data/faiss_db", hf)
    db3 = api.api_vectorStores.getfaissdb("data/faiss_db", hf)
    query = "2023년 재건축시장 동향은 어떻게 될까요?"

    docs = db3.max_marginal_relevance_search(
        query, k=3, fetch_k=10, lambda_mult=0.5)
    # 10개의 문서를 상위 3개의 문서로 줄임, lambda_mult는 0~1 다양성~유사도설정
    print("question:{} \n".format(query))
    for i in range(len(docs)):
        print("{}번째 유사문서".format(i+1))
        print("-"*100)
        print(docs[i].page_content)
        print("\n")
        print(docs[i].metadata)
        print("-"*100)


if __name__ == "__main__":
    # createDB()
    maxMargin()
