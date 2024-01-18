

def charsplit(pages,chunk_size,chunk_overlap,length_function,separator):
    from langchain.text_splitter import CharacterTextSplitter
    text_splitter=CharacterTextSplitter(
        separator="\n\n",
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len
    )

    return text_splitter.split_text(pages)

def recursivesplit(pages,chunk_size,chunk_overlap,length_function):
    # RecursiveCharacterTextSplitter를 사용한 경우
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    import api_misc

    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=api_misc.tiktoken_len
    )

    return text_splitter.split_documents(pages)


def languagesplit(code,language,chunk_size,chunk_overlap):
    # python_code="""
    # def hello_world():
    #     print("Hello World!")
    # hello_world()
    # """
    from langchain.text_splitter import (RecursiveCharacterTextSplitter,Language)
    python_splitter=RecursiveCharacterTextSplitter.from_language(language=language,chunk_size=50,chunk_overlap=0)
    return python_splitter.create_documents([code])