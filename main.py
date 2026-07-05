from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

STUDENT_DATA = [
    {
        "id": 101,
        "name": "Ganesh Sharma",
        "age": 22,
        "sex": "Male",
        "latest_qualification": "Undergraduate"
    },
    {
        "id": 102,
        "name": "Preeti Sharma",
        "age": 21,
        "sex": "Female",
        "latest_qualification": "Undergraduate"
    },
    {
        "id": 103,
        "name": "Rekha Jain",
        "age": 26,
        "sex": "Female",
        "latest_qualification": "Postgraduate"
    }
]

@app.get(path = "/")
def home():
    return {
        "message": "Welcome to Student Management API, build by Sharma Enterprises."
    }

@app.get("/student/{student_id}")
def student_info(student_id: int):
    if student_id == 101:
        return {
            "id": 101,
            "name": "Ganesh Sharma",
            "age": 22,
            "sex": "Male",
            "latest_qualification": "Undergraduate"
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

