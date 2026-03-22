from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# Variables de entorno (las define docker-compose)
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))

client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
db = client["test_db"]
collection = db["items"]

@app.get("/")
def root():
    return {"mensaje": "API conectada a MongoDB"}

@app.post("/items")
def create_item(name: str):
    item = {"name": name}
    collection.insert_one(item)
    return {"mensaje": "Item guardado", "item": item}

@app.get("/items")
def get_items():
    items = list(collection.find({}, {"_id": 0}))
    return items
