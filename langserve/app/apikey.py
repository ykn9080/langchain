import os
from dotenv import load_dotenv

   
def getOpenai():
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    os.environ["OPENAI_API_KEY"] = api_key
    return api_key

def getserpapi():
    load_dotenv()
    serpapi_key = os.getenv('SERPAPI_API_KEY')
    os.environ["SERPAPI_API_KEY"] = serpapi_key
    return serpapi_key
def getgoogle():
    load_dotenv()
    google_key = os.getenv('GOOGLE_API_KEY')
    os.environ["GOOGLE_API_KEY"] = google_key
    return google_key
def getpinecone():
    load_dotenv()
    pinecone_key = os.getenv('PINECONE_API_KEY')
    os.environ["PINECONE_API_KEY"] = pinecone_key
    return pinecone_key

def gethuggingface():
    load_dotenv()
    huggingface_key = os.getenv('HUGGINGFACEHUB_API_TOKEN')
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_key
    return huggingface_key