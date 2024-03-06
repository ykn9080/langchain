from langchain_community.llms import Ollama

llm = Ollama(model="llama2")

# print(llm.invoke("Tell me a joke"))

query = "Tell me a joke"

for chunks in llm.stream(query):
    print(chunks)