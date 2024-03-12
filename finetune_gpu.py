from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import RetrievalQAWithSourcesChain
from llama_index.readers.file import PyMuPDFReader
from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
import re
from langchain.llms import GradientLLM
import warnings
from langchain.embeddings import HuggingFaceEmbeddings
import jsonlines
from datasets import Dataset
from config.apikey import getGradient,gethuggingface



bergerking_dataset = []
with jsonlines.open("data/burger/qa_버거킹_train.jsonl") as f:
    for line in f.iter():
      # bergerking_dataset.append(f'<s>[INST] {line["inputs"]} [/INST] {line["response"]} </s>')
      bergerking_dataset.append(f'<s>### Instruction: \n{line["inputs"]} \n\n### Response: \n{line["response"]}</s>')

# 데이터셋 확인
print('데이터셋 확인')
print(f'데이터넷 확인 {bergerking_dataset[:5]}')

# 데이터셋 생성 및 저장
burgerking_dataset = Dataset.from_dict({"text": bergerking_dataset})
burgerking_dataset.save_to_disk('data/burger/burgerking_dataset')

# 데이터셋 info 확인
print('데이터셋 info 확인')
print(burgerking_dataset)