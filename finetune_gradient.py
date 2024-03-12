# from llama_index.llms.gradient import GradientModelAdapterLLM
from llama_index.llms.gradient import GradientModelAdapterLLM
from llama_index.llms.gradient import GradientBaseModelLLM
from llama_index.finetuning import GradientFinetuneEngine
import warnings
from config.apikey import getGradient,gethuggingface
import sys
"""
import os
import gdown
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
from langchain.embeddings import HuggingFaceEmbeddings
from datasets import Dataset
import jsonlines
"""




warnings.filterwarnings('ignore')

getGradient()
gethuggingface()

# os.environ["GRADIENT_ACCESS_TOKEN"] = ''
# os.environ["GRADIENT_WORKSPACE_ID"] = ""
# os.environ["model_adapter_id"] = ""
# os.environ["huggingface_token"] = ""

# sample 데이터를 가져다 로컬에 저장
"""
gdown.download(url="https://drive.google.com/file/d/16hHL4hLer3nWhX18STvr061LcHzfFgN2/view?usp=sharing", output="data/burger/qa_버거킹_train.jsonl", quiet=False)
gdown.download(url="https://drive.google.com/file/d/1nB6ERfII2ODEDS_1xY3C5TBZHeOMMcPI/view?usp=sharing", output="data/burger/qa_버거킹_train_ko.jsonl", quiet=False)
gdown.download(url="https://drive.google.com/file/d/11U7let6PY_YCJpgRT0Dpr5DXSO3Ceqep/view?usp=sharing", output="data/burger/버거킹.pdf", quiet=False)
gdown.download(url="https://drive.google.com/file/d/1BifMUDNX2v_4B7hb4YHv6eDinQqAjTZK/view?usp=sharing", output="data/burger/Burger-King.pdf", quiet=False)
"""

def main():
    print(sys.argv)
    if(len(sys.argv)<2):
        base_model_slug = "llama2-7b-chat"
        base_llm = GradientBaseModelLLM(
            base_model_slug=base_model_slug, max_tokens=500, is_chat_model=True
        )

        finetune_engine = GradientFinetuneEngine(
            base_model_slug=base_model_slug,
            name="bugurking",
            data_path="data/burger/qa_버거킹_train.jsonl",
            verbose=True,
            max_steps=200,
            batch_size=1,
        )
        print(finetune_engine.model_adapter_id)

        # 파인튜닝 2 epoch만
        epochs = 2
        for i in range(epochs):
            print(f"** EPOCH {i} **")
            finetune_engine.finetune()

        # 파인튜닝한 모델 사용
        llm = finetune_engine.get_finetuned_model(
        max_tokens=500, is_chat_model=False
        )
    else:
        # 이미 파인튜닝되어 있으면 아래와 같이 사용
        llm = GradientModelAdapterLLM(
            model_adapter_id=sys.argv[1],
            max_tokens=500,
        )
    
    # 3가지 버거킹 메뉴를 추천해 달라는 내용으로 모델 테스트
    completion=llm.complete('Recommend only 3 items from Burger King’s menu.').text
    print(completion)
if __name__ == "__main__":
    main()