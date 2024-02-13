import pathlib
import textwrap
import streamlit as st
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from config import getGemini

key = getGemini()
genai.configure(api_key=key)


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("인생이란 무엇인가?")
# md = to_markdown(response.text)

# st.write(response.text)

response = model.generate_content(
    "https://github.com/FinanceData/FinanceDataReader를 참조하여 삼성전자 주식 데이터를 가져오는 python코드를 작성해보세요")
st.write(response.text)
