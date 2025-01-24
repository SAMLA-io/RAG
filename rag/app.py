# Written by Juan Pablo Gutiérrez
# 10/01/2025
# This script is the main entry point for the RAG system

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.database import router

app = FastAPI()

origins = ["*"]

app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
async def test():
 return "Hello World!"

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)