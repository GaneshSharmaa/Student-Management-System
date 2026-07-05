from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get(path = "/api/")
def home():
    return {
        "message": "Welcome to Student Management API, build by Sharma Enterprises."
    }

@app.get("/api/about")
def about():
    return {
        "project-name": "Student Management System",
        "created-by": "Sharma Enterprises",
        "developer": "Ganesh Sharma",
        "current-version": "v1.0"
    }

@app.get("/api/contact")
def contact():
    return {
        "email": "ganesh27sharma09@gmail.com",
        "mobile": "90xxx-99xxx",
        "website": "https://ganeshsharma.tech"
    }

