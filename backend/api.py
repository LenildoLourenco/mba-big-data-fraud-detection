from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = "output/fraudes"

def load_data():
    dados = []
    if not os.path.exists(DATA_PATH):
        return []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".json"):
            with open(os.path.join(DATA_PATH, file)) as f:
                for line in f:
                    dados.append(json.loads(line))
    return dados

@app.get("/fraudes")
def get_fraudes():
    return load_data()

@app.get("/fraudes/top")
def get_top_fraudes():
    data = load_data()
    return sorted(data, key=lambda x: x["valor"], reverse=True)[:50]