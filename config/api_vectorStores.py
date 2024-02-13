from langchain_community.vectorstores import Pinecone
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores import FAISS
import pinecone
import apikey

def getdb(dbtype,embedding,pdir):
    if(dbtype=="pinecone"):
        # pdir=index_name("yknam-sample")
        return getpinecone(pdir,embedding)
    elif(dbtype=="chroma"):
        return getchromadb(pdir,embedding)
    elif(dbtype=="faiss"):
        return getfaissdb(pdir,embedding)
    else:
        return None
def setdb(dbtype,docs,embedding,pdir):
    if(dbtype=="pinecone"):
        # pdir=index_name("yknam-sample")
        return setpinecone(docs,embedding,pdir)
    elif(dbtype=="chroma"):
        return setchromadb(docs,embedding,pdir)
    elif(dbtype=="faiss"):
        return setfaissdb(docs,embedding,pdir)
    else:
        return None
    
def setpinecone(docs,embedding,index_name="yknam-sample"):
    pinecone.init(
        api_key=apikey.getpinecone(),
        environment="gcp-starter"
    )
    index=Pinecone.from_documents(docs,embedding,index_name=index_name)
    return index

def getpinecone(index_name,embedding,):
    pinecone.init(
        api_key=apikey.getpinecone(),
        environment="gcp-starter"
    )
    index = Pinecone.from_existing_index(index_name, embedding)

    return index
def getchromadb(pdir,embedding):
    
    return Chroma(persist_directory=pdir,embedding_function=embedding)

def setchromadb(docs,embedding,pdir):
    
    if(pdir!=None):
        index=Chroma.from_documents(docs,embedding,persist_directory=pdir)
    else:
        index=Chroma.from_documents(docs,embedding)

    return index

def setfaissdb(docs,embedding,pdir):
    if(pdir==None):
        db3=FAISS.from_documents(docs, embedding)
    else:
        db3=FAISS.from_documents(docs, embedding)
        db3.save_local(pdir)
    return db3
def getfaissdb(pdir,embeddings):
    return FAISS.load_local(pdir,embeddings)