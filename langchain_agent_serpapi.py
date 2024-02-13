from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.load.dump import dumps
from langchain_openai import OpenAI
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
prompt = "한국말로 답해줘. 가수 RAIN의 아내가 누구야? 그녀의 나이에 0.37을 곱하면? "
# response = agent.run(prompt) # verbose를 True로 하여 화면에 출력
response = agent({"input": prompt})  # verbase를 intermediate_step 변수에 담기

print(dumps(response["intermediate_steps"], pretty=True))
print(response["output"])
