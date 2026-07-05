from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get(path = "/")
def home():
    return "Hello!"
