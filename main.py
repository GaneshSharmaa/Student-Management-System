from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get(path = "/")
def home():
    return {
        "message": "Welcome to Student Management API, build by Sharma Enterprises."
    }

@app.get("/about")
def about():
    return {
        "project-name": "Student Management System",
        "created-by": "Sharma Enterprises",
        "developer": "Ganesh Sharma",
        "current-version": "v1.0"
    }

