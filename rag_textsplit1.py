import api_misc
from config import api_document
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
with open('data/state_of_the_union.txt', 'r') as f:
    state_of_the_union = f.read()
    # print(text[:100])
    # print('-----------------')
    # print(text[-100:])

from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=100,
    length_function=len
)

texts = text_splitter.split_text(state_of_the_union)
# print(texts[0])
# print('-----------------')
# print(texts[1])
# print('-----------------')
# print(texts[2])

char_list = []
for i in range(len(texts)):
    char_list.append(len(texts[i]))  # 각 chunk의 글자수를 리스트에 저장
# print(char_list)

# RecursiveCharacterTextSplitter를 사용한 경우
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    length_function=len
)

texts = text_splitter.create_documents([state_of_the_union])
# print(texts[0].page_content)
# print('-'*100)
# print(texts[1].page_content)

char_list = []
for i in range(len(texts)):
    char_list.append(len(texts[i].page_content))  # 각 chunk의 글자수를 리스트에 저장
# print(char_list)


texts = text_splitter.split_documents


# text_splitter.create_documents([text])

# loader=PyPDFLoader("data/realestate.pdf")
pages = api_document.pdf_loader("data/realestate.pdf")
# pages=loader.load_and_split() # document객체 생성
# print(len(pages))
print(pages[0].page_content)

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=100,
    length_function=len
)

texts = text_splitter.split_documents(pages)
# print(texts[0].page_content)


# tokerizer 사용
# import tiktoken
# tokenizer=tiktoken.get_encoding("cl100k_base")

# def tiktoken_len(text):
#     tokens=tokenizer.encode(text)
#     return len(tokens)

# print(tiktoken_len(texts[1].page_content))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0,
    length_function=api_misc.tiktoken_len
)

texts = text_splitter.split_documents(pages)

print(texts[0].page_content)
print(api_misc.tiktoken_len(texts[0].page_content))
