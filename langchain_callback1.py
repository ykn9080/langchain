from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from api import apikey

apikey.getOpenai()
model = ChatOpenAI(model="gpt-4")

with get_openai_callback() as callback:
    result=model.invoke("고객 중 가장 많이 지불한 사람과 금액을 알려줘?")
    print(result)
    print("-"*100)
    print(callback)