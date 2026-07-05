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
        "project_name": "Student Management System",
        "created_by": "Sharma Enterprises",
        "developer": "Ganesh Sharma",
        "current_version": "v1.0"
    }

@app.get("/contact")
def contact():
    return {
        "email": "ganesh27sharma09@gmail.com",
        "mobile": "90xxx-99xxx",
        "website": "https://ganeshsharma.tech"
    }

