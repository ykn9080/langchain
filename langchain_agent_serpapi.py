from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import apikey
import os

apikey.getOpenai()
apikey.getserpapi()

llm = OpenAI(temperature=0)

tools=load_tools(["serpapi","llm-math"],llm=llm)
#agenttype="react_docstore" 
#agenttype="self-ask-with-search"
agenttype="zero-shot-react-description"
agent=initialize_agent(tools,llm,agent=agenttype,verbose=True)

agent.run("한국말로 답해줘. 가수 RAIN의 아내가 누구야? 그녀의 나이에 0.37을 곱하면? ")





