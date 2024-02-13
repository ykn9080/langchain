from langchain.callbacks import StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from config import getOpenai

getOpenai()

handler = StdOutCallbackHandler()
llm = OpenAI()
prompt = PromptTemplate.from_template("1 + {number} = ")

# # Constructor callback: First, let's explicitly set the StdOutCallbackHandler when initializing our chain
# chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler])
# chain.run(number=2)

# Use verbose flag: Then, let's use the `verbose` flag to achieve the same result
chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
rtn = chain.run(number=2)
print(rtn)

# # Request callbacks: Finally, let's use the request `callbacks` to achieve the same result
# chain = LLMChain(llm=llm, prompt=prompt)
# rtn = chain.run(number=2, callbacks=[handler])
# print(rtn)
