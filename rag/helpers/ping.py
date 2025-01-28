# Written by Juan Pablo Gutiérrez
# 10/01/2025
# This script pings the MongoDB Atlas cluster to confirm a successful connection

import os
from pymongo import MongoClient
import dotenv

dotenv.load_dotenv()

def ping_db():
    client = MongoClient(os.getenv("MONGO_URI"))
    client.admin.command('ping')
    return "Pinged your deployment. You successfully connected to MongoDB!"
