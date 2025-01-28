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
    try:
        return {
            "statusCode": "200",
            "body" : ping_db()
        }
    except Exception as e:
        return {
            "statusCode": "500",
            "body" : f"Error pinging database: {e}"
        }

@router.get("/create_index")
async def create_index_route(database: str, collection: str, dimensions: int):
    try:
        return {
            "statusCode": "200",
            "body" : create_index(database, collection, dimensions)
        }
    except Exception as e:
        return {
            "statusCode": "500",
            "body" : f"Error creating index: {e}"
        }

@router.get("/ask")
async def ask_route(database: str, collection: str, query: str):
    try:
        return {
            "statusCode": "200",
            "body" : prompt_llm(query, database, collection)
        }
    except Exception as e:
        return {
            "statusCode": "500",
            "body" : f"Error asking: {e}"
        }

@router.get("/upload_documents")
async def upload_documents_route(database: str, collection: str, document_content: str, document_metadata: str):
    try:
        return {
            "statusCode": "200",
            "body" : upload_documents(database, collection, document_content, document_metadata)
        }
    except Exception as e:
        return {
            "statusCode": "500",
            "body" : f"Error uploading documents: {e}"
        }

@router.get("/get_context")
async def get_context_route(database: str, collection: str, query: str):
    try:
        return {
            "statusCode": "200",
            "body" : get_rag_context(query, database, collection)
        }
    except Exception as e:
        return {
            "statusCode": "500",
            "body" : f"Error getting context: {e}"
        }
