import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.llms import OpenAI
from langchain.schema import HumanMessage
from langchain.schema import BaseOutputParser
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
from config import getOpenai

getOpenai()
chatModel = ChatOpenAI()


class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list of items."""

    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(", ")


print(CommaSeparatedListOutputParser().parse("a, b, c"))


template = """
당신은 쉼표로 구분된 목록을 생성하는 조수입니다.\
사용자가 카테고리를 전달하면 해당 카테고리에 속하는 5개의 객체를 쉼표로 구분된 목록으로 반환합니다.\
오직 쉼표로 구분된 목록만 반환해야 합니다.\
"""
human_template = "{text}"
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template)
])
chain = chat_prompt | chatModel | CommaSeparatedListOutputParser()
rtn = chain.invoke({"text": "색깔"})
print(rtn)
