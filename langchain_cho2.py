

import streamlit as st
# from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

# load_dotenv()
#api_key = os.getenv('OPENAI_API_KEY')
# # print(api_key)
# # chatModel = ChatOpenAI(openai_api_key=api_key)

# chatModel = ChatOpenAI()
# result = chatModel.predict(" hi! ")
# print(result)

# col1,col2=st.columns([1,2])
# with col1:
title = st.text_input('Message','Who invented the hangul?')
# with col2:
#     #st.image('https://www.fool.com.au/wp-content/uploads/2019/12/Netflix-logo.jpg')
#     st.title('Favorite *movies!* :sunglasses:')
#     uploaded_file = st.file_uploader("Choose a file")
#     st.camera_input("Camera input")

# col2.markdown('## :movie_camera: Movie Recommendation')

if st.button('Send'):
    llm=OpenAI()
    with st.spinner("Predicting..."):
        result=llm.predict(title)

    # chatModel = ChatOpenAI()
    # result = chatModel.predict(title)
    print(result)
    # with col2:
    st.write(result)


