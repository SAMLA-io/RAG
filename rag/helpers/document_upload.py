# Written by Juan Pablo Gutiérrez
# 10/01/2025
# This script is the helper for the document upload

import os
import dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from uuid import uuid4
from langchain_core.documents import Document

dotenv.load_dotenv()

MONGODB_ATLAS_CLUSTER_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)

def upload_documents(database, collection, document_content, document_metadata):

    documents = [Document(page_content=document_content, metadata=document_metadata)]
    uuids = [str(uuid4()) for _ in range(len(documents))]

    index_name = f"{database}_{collection}_index"
    collection = client[database][collection]
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    
    vector_store = MongoDBAtlasVectorSearch(
        collection=collection,
        embedding=embeddings,
        index_name=index_name,
        relevance_score_fn="cosine",
    )

    try:
        vector_store.add_documents(documents=documents, ids=uuids)
    except Exception as e:
        return {
            "statusCode": "500",
            "body" : f"Error uploading documents: {e}"
        }

    return {
        "statusCode": "200",
        "body" : "Documents uploaded successfully"
    }

