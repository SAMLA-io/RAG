# Written by Juan Pablo Gutiérrez
# 10/01/2025
# This script creates a vector search index for a given database and collection

import os
import dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
dotenv.load_dotenv()

MONGODB_ATLAS_CLUSTER_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)

def create_index(database, collection, dimensions=3072):
    index_name = f"{database}_{collection}_index"
    collection = client[database][collection]
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    
    vector_store = MongoDBAtlasVectorSearch(
        collection=collection,
        embedding=embeddings,
        index_name=index_name,
        relevance_score_fn="cosine",
    )

    vector_store.create_vector_search_index(dimensions=dimensions)
 
    return "Index created successfully"
