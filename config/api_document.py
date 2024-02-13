from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import WebBaseLoader
from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import CSVLoader
import sys

def pdf_loader(url):
    if url=="":
        url="data/realestate.pdf"
    loader = PyPDFLoader(url)
    pages = loader.load_and_split()
    print(pages[0].page_content)
    return pages

def web_loader(url):
    if url=="": 
        url="https://n.news.naver.com/mnews/article/092/0002307222?sid=105"
    loader=WebBaseLoader(url)
    pages = loader.load()
    print(pages[0].page_content)
    return pages

def unstructured_loader(url):
    if url=="":
        url=["https://n.news.naver.com/mnews/article/092/0002307222?sid=105","https://n.news.naver.com/mnews/article/052/0001944792?sid=105"]
    loader=UnstructuredURLLoader(urls=url)
    pages = loader.load()
    print(pages)
    return pages

def docx2txt_loader(url):
    if url=="":
        url="data/202312_monthlyreport.docx"
    loader=Docx2txtLoader(url)
    pages = loader.load()
    print(pages[0].page_content)
    return pages

csvargs={
            'delimiter':',',
            'quotechar':'"',
            'fieldnames': ['height','weight','success_field_goals','success_free_throws','avg_points_scored']
        }
def csv_loader(url,csvargs):
    if url=="":
        url="data/basketball.csv"
    loader=CSVLoader(file_path=url, csv_args=csvargs)
    pages = loader.load()
    print(pages[:10])
    return pages

if __name__ == "__main__":
    func=sys.argv[1]
    url=""
    csvargs=""

    if len(sys.argv)>2:
        url=sys.argv[2]
    if len(sys.argv)>3:
        csvargs=sys.argv[3]

    if func == "pdf":
        pdf_loader(url)
    elif func == "web":
        web_loader(url)
    elif func == "unstructured":
        unstructured_loader(url)
    elif func == "docx2txt":
        docx2txt_loader(url)
    elif func == "csv":
        csv_loader(url,csvargs)
    else:
        print("not supported function")