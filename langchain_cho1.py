#! /usr/bin/python3

from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI

load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY')
# print(api_key)

#chatModel = ChatOpenAI(openai_api_key=api_key)
content='겨울';
chatModel = ChatOpenAI()
#result = chatModel.predict(content+" 에 대한 시를 써줘")
result = chatModel.predict("Who are you?")
print(result)