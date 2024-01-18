import uvicorn
from fastapi import FastAPI
from langcorn import create_service

app: FastAPI = create_service(
    # title="Langcorn",
    # description="Langcorn is a language model chain for natural language processing.",
    # version="0.1.0",
    # openapi_url="/api/v1/openapi.json",
    # docs_url="/api/v1/docs",
    # redoc_url="/api/v1/redoc",

)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8009, reload=True, workers=1)
