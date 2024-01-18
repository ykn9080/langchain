#! /bin/python3
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatAnthropic, ChatOpenAI
from langserve import add_routes
import os
from dotenv import load_dotenv
import openai

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = api_key
os.environ["ANTHROPIC_API_KEY"] = api_key

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
)

add_routes(
    app,
    ChatAnthropic(),
    path="/anthropic",
)

model = ChatAnthropic()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
add_routes(
    app,
    prompt | model,
    path="/joke",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8018)