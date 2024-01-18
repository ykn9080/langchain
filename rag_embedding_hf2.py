# 한글되는 huggingface 모델을 이용한 BGE 예제

from langchain.embeddings import HuggingFaceBgeEmbeddings

from numpy import dot
from numpy.linalg import norm
import numpy as np

def cos_sim(A,B):
    return dot(A,B)/(norm(A)*norm(B))

model_name="jhgan/ko-sbert-nli"
model_kwargs={'device':'cpu'}
encode_kwargs={'normalize_embeddings':True} 
hf=HuggingFaceBgeEmbeddings(model_name=model_name,model_kwargs=model_kwargs,encode_kwargs=encode_kwargs)

embeddings=hf.embed_documents([
    "안녕하세요",
    "제 이름은 홍길동입니다.",
    "이름이 뭐예요?",
    "랭체인은 유용합니다.",
    "홍길동 아버지의 이름은 홍상직입니다."
])
q="홍길동은 아버지를 아버지라 부르지 못했다. 홍길동 아버지의 이름은 무엇인가?"
a="홍길동의 아버지는 엄했습니다."
BGE_query_q=hf.embed_query(q)
BGE_query_a=hf.embed_query(a)

print(cos_sim(BGE_query_q,BGE_query_a))
print(cos_sim(BGE_query_q,embeddings[3]))
print(cos_sim(BGE_query_q,embeddings[4]))
