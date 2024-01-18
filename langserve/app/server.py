from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
import apikey

app = FastAPI()
apikey.gethuggingface()

llm=HuggingFaceHub(repo_id="google/flan-t5-large",model_kwargs={"temperature":0})

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, llm,path="/base")


prompt=PromptTemplate.from_template("What is {topic}")
add_routes(
    app,
    prompt | llm,
    path="/demo"
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8882)
