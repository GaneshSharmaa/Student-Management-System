from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get(path = "/")
def home():
    return {
        "message": "Welcome to Student Management API, build by Sharma Enterprises."
    }

