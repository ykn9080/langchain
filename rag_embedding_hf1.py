from langchain.embeddings import HuggingFaceBgeEmbeddings
import apikey
from numpy import dot
from numpy.linalg import norm
import numpy as np

def cos_sim(A,B):
    return dot(A,B)/(norm(A)*norm(B))

model_name="BAAI/bge-small-en"
model_kwargs={'device':'cpu'}
encode_kwargs={'normalize_embeddings':True} 
hf=HuggingFaceBgeEmbeddings(model_name=model_name,model_kwargs=model_kwargs,encode_kwargs=encode_kwargs)

embeddings=hf.embed_documents([
    "today is a good day",
    "weathers are good",
    "I like pizza",
    "I like hamburgers",
    "I like hotdogs",
    "I like chicken",
    "my name is morris"
])
BGE_query_q=hf.embed_query("What is your favorite food?")
BGE_query_a=hf.embed_query("I like a steak")

print(cos_sim(BGE_query_q,BGE_query_a))
print(cos_sim(BGE_query_q,embeddings[1]))
print(cos_sim(BGE_query_q,embeddings[3]))
