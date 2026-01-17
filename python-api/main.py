from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {
        "mensaje": "API funcionando correctamente",
        "fecha": datetime.now().isoformat()
    }

@app.get("/info")
def info():
    return {
        "nombre_app": "API de ejemplo",
        "version": "1.0",
        "autor": "Josias Maidana"
    }
