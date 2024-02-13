import sys
sys.path.append("/home/yknam/ipykernel")
from langchain.text_splitter import (RecursiveCharacterTextSplitter, Language)
from config import api_textsplit

print(RecursiveCharacterTextSplitter.get_separators_for_language(Language.PYTHON))

python_code = """
def hello_world():
    print("Hello World!")
hello_world()
"""

# python_splitter=RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON,chunk_size=50,chunk_overlap=0)
pages = api_textsplit.languagesplit(python_code, Language.PYTHON, 50, 0)
# python_docs=python_splitter.create_documents([python_code])

print(pages)
