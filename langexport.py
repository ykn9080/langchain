#!/usr/bin/python3

from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(api_key)

chatModel = ChatOpenAI(openai_api_key=api_key)
result = chatModel.predict(" hi! ")
print(result)



