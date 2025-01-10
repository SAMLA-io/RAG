# Written by Juan Pablo Gutiérrez
# 10/01/2025
# This script pings the MongoDB Atlas cluster to confirm a successful connection

import os
from pymongo import MongoClient
import dotenv

dotenv.load_dotenv()

def ping_db():
    client = MongoClient(os.getenv("MONGO_URI"))
    try:
        client.admin.command('ping')

        return {
            "statusCode": "200",
            "body" : "Pinged your deployment. You successfully connected to MongoDB!"
        }
    except Exception as e:
        return {
            "statusCode": "500",
            "body" : f"Error pinging database: {e}"
        }
