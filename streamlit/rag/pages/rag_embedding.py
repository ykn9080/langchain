import numpy as np
from numpy.linalg import norm
from numpy import dot
from langchain_openai import OpenAIEmbeddings
from config import getOpenai

getOpenai()

embeddings_model = OpenAIEmbeddings()

embeddings = embeddings_model.embed_documents(["안녕하세요. 저는 한국어를 잘 못해요.",
                                               "제 이름은 김철수입니다.",
                                              "이름이 뭐예요?",
                                               "랭체인은 유용합니다.",
                                               "hello world!"])
print(len(embeddings), len(embeddings[0]))

embedding_query_q = embeddings_model.embed_query("이 대화에서 언급된 이름은 뭐예요?")
embedding_query_a = embeddings_model.embed_query("이 대화에서 언급된 이름은 김철수다.")
print(len(embedding_query_q), len(embedding_query_a))


def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))


print(cos_sim(embedding_query_q, embedding_query_a))
print(cos_sim(embedding_query_q, embeddings[1]))
print(cos_sim(embedding_query_q, embeddings[3]))
