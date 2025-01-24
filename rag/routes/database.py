# Written by Juan Pablo Gutiérrez
# 10/01/2025
# This script is the API router for the RAG system

from fastapi import APIRouter
from ..helpers.ping import ping_db
from ..helpers.create_index import create_index
from ..helpers.rag import prompt_llm, get_rag_context
from ..helpers.document_upload import upload_documents
router = APIRouter()

@router.get("/ping")
async def ping():
    return ping_db()

@router.get("/create_index")
async def create_index(database: str, collection: str, dimensions: int):
    return create_index(database, collection, dimensions)

@router.get("/ask")
async def ask(database: str, collection: str, query: str):
    return prompt_llm(query, database, collection)

@router.get("/upload_documents")
async def upload(database: str, collection: str, document_content: str, document_metadata: str):
    return upload_documents(database, collection, document_content, document_metadata)

@router.get("/get_context")
async def get_context(database: str, collection: str, query: str):
    return get_rag_context(query, database, collection)
