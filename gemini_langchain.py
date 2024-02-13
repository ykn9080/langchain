import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import getGemini

GOOGLE_API_KEY = getGemini()

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate.from_template(template)

chain = prompt | llm


question = "How much is 2+2?"
print(chain.invoke({"question": question}))
    
# print(
#     llm.invoke(
#         "What are some of the pros and cons of Python as a programming language?"
#     )
# )
# result = llm.invoke("Write a ballad about LangChain")
# print(result.content)

# tweet_prompt = PromptTemplate.from_template("You are a content creator. Write me a tweet about {topic}.")

# tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)

# if __name__=="__main__":
#     topic = "how ai is really cool"
#     resp = tweet_chain.run(topic=topic)
#     print(resp)