from langchain.chains import LLMMathChain, RetrievalQA
from langchain.agents import Tool, load_tools
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.utilities import SerpAPIWrapper
from langchain.tools import DuckDuckGoSearchRun
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import pandas as pd
from config import getOpenai
import warnings
warnings.filterwarnings("ignore")

getOpenai()

search_tool = DuckDuckGoSearchRun()

# model
model = ChatOpenAI(temperature=0)
# prompt
# from langchain import PromptTemplate

# memory
memory = ConversationBufferMemory(
    memory_key='chat_history', return_messages=True)
# tools
tools = [Tool(name="DuckDuckGoSearchRun", func=search_tool.run,
              description="Useful when you need to answer questions about current events.")]
# agent
# from langchain_experimental.agents import create_pandas_dataframe_agent

agent_chain = initialize_agent(
    tools=tools,
    memory=memory,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    llm=model
)
print(search_tool.run('대한민국 대통령 이름'))
