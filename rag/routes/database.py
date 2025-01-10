from fastapi import APIRouter
from helpers.ping import ping_db
from helpers.create_index import create_index
from helpers.rag import prompt_llm

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