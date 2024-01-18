
# |Good parts:
# |1. The code imports necessary modules and classes, indicating that it follows modular programming principles.
# |2. The code uses a callback handler, `StreamingStdOutCallbackHandler`, which suggests that it can handle streaming output efficiently.
# |3. The code initializes an instance of the `ChatOpenAI` class, passing appropriate parameters such as temperature, max_tokens, and model_name.
# |4. The code sets the streaming parameter to True, indicating that it can handle streaming input.
# |5. The code calls the `predict` method of the `ChatOpenAI` instance, passing a prompt to generate a response.
# |
# |Bad parts:
# |1. The code imports `apikey` module but does not use it correctly. It calls `apikey.getOpenai()` without assigning the returned value to any variable or using it in the subsequent code. This suggests that the code may not be functioning as intended.
# |2. The code does not handle any exceptions or errors that may occur during the execution. It would be better to include appropriate error handling mechanisms to ensure the code's robustness.
# |3. The code does not include any comments or documentation to explain the purpose and functionality of the different parts. Adding comments would improve code readability and maintainability.
# |4. The code does not follow consistent naming conventions. For example, `llm` is not a descriptive variable name and does not follow the recommended lowercase_with_underscores naming style.
# |
# |Overall, the code seems to have some issues related to the usage of the `apikey` module and lacks proper error handling and documentation.
# |
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from api import apikey

apikey.getOpenai()

# 객체 생성
llm = ChatOpenAI(temperature=0,               # 창의성 (0.0 ~ 2.0)
                 max_tokens=2048,             # 최대 토큰수
                 model_name='gpt-3.5-turbo',  # 모델명
                 streaming=True,
                 callbacks=[StreamingStdOutCallbackHandler()]
                 )
llm.predict("대한민국 제 3의 도시는?")
