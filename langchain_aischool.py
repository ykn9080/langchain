

import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

load_dotenv()
#api_key = os.getenv('OPENAI_API_KEY')
# # print(api_key)
# # chatModel = ChatOpenAI(openai_api_key=api_key)

# chatModel = ChatOpenAI()
# result = chatModel.predict(" hi! ")
# print(result)

# col1,col2=st.columns([1,2])
# with col1:
title = st.text_input('이름생성명','online service')
# with col2:
#     #st.image('https://www.fool.com.au/wp-content/uploads/2019/12/Netflix-logo.jpg')
#     st.title('Favorite *movies!* :sunglasses:')
#     uploaded_file = st.file_uploader("Choose a file")
#     st.camera_input("Camera input")

# col2.markdown('## :movie_camera: Movie Recommendation')
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate


# prompt=PromptTemplate.from_examples()
# st.write(prompt)
prompt=PromptTemplate.from_template("{product}를 만드는 회사의 이름을 추천해줘?")

if st.button('Send'):
    llm=OpenAI()
    with st.spinner("Predicting..."):
        prod=prompt.format(product=title)
        msgs=[HumanMessage(content=prod)]
        #result=llm.predict(title)
        result=llm.predict_messages(msgs)

        # chatModel = ChatOpenAI()
        # result1 = chatModel.predict_messages(msgs)
    #print(result)
    # with col2:
    st.write(result)
    # st.write(result1)


