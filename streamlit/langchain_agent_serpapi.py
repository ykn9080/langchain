# from config.apikey import getOpenai, getserpapi
import streamlit as st
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.load.dump import dumps
from langchain_openai import OpenAI
import sys
sys.path.append("..")
from config import getOpenai, getserpapi

getOpenai()
getserpapi()

llm = OpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm=llm)
# agenttype="react_docstore"
# agenttype="self-ask-with-search"
agenttype = "zero-shot-react-description"
agent = initialize_agent(tools, llm, agent=agenttype,
                         verbose=False, return_intermediate_steps=True)

# rtn = agent.run("한국말로 답해줘. 가수 RAIN의 아내가 누구야? 그녀의 나이에 0.37을 곱하면? ")
response = agent({"input": "한국말로 답해줘. 가수 RAIN의 아내가 누구야? 그녀의 나이에 0.37을 곱하면? "})

st.write(dumps(response["intermediate_steps"], pretty=True))
st.write(response["output"])


if __name__ == '__main__' :
    pass