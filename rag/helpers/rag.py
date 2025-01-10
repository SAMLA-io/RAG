# Written by Juan Pablo Gutiérrez 
# 10/01/2025
# This script is a the main body for the RAG (Retrieval Augmented Generation) system

import os
import dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, RetrievalQA
from openai import OpenAI

dotenv.load_dotenv()

MONGODB_ATLAS_CLUSTER_URI = os.getenv("MONGO_URI")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)

def prompt_llm(query, database, collection):
    global client

    search_index_name = f"{database}_{collection}_index"

    collection = client[database][collection]

    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    vector_store = MongoDBAtlasVectorSearch(
        collection=collection,
        embedding=embeddings,
        index_name=search_index_name,
        relevance_score_fn="cosine",
    )

    search_results = vector_store.similarity_search(query, k=2)
    docs_content = "\n\n".join(doc.page_content for doc in search_results)
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    messages = [
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "system", "content": "Context: {}".format(docs_content) },
        { "role": "user", "content": "How's the stock market doing?" },
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )

    return {
        "statusCode": "200",
        "body": response.choices[0].message.content
    }
