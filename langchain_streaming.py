

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_openai import ChatOpenAI
from config import getOpenai

getOpenai()

# 객체 생성
llm = ChatOpenAI(temperature=0,               # 창의성 (0.0 ~ 2.0)
                 max_tokens=2048,             # 최대 토큰수
                 model_name='gpt-3.5-turbo',  # 모델명
                 streaming=True,
                 callbacks=[StreamingStdOutCallbackHandler()]
                 )
llm.invoke("대한민국 제 3의 도시는?")
