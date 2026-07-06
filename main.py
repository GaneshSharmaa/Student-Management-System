# importing the modules
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# importing the data from the file
from student_information.student_data import STUDENT_DATA
from student_information.semester_data import SEMESTER_1

# initializing the application
app = FastAPI()

# HOME PAGE ROUTE
@app.get(path = "/")
def home():
    return {
        "message": "Welcome to Student Management API, build by Sharma Enterprises."
    }

# EACH STUDENT INFO PAGE ROUTE
@app.get("/student/{student_id}")
def student_info(student_id: int):
    for each_student in STUDENT_DATA:
        if student_id == each_student["id"]: 
            return each_student

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Student with ID {student_id} not found!")

# EACH SEMESTER DETAILS PAGE ROUTE
@app.get("/student/{student_id}/semester/{semester}")
def student_semester_detail(student_id: int, semester: int):
    for each_student_marks in SEMESTER_1:
        if student_id == each_student_marks["id"] and semester == 1:
            return student_info(student_id) | each_student_marks
    
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Marks of Semester {semester} ID {student_id} not found!")

# ABOUT PAGE ROUTE
@app.get("/about")
def about():
    return {
        "project_name": "Student Management System",
        "created_by": "Sharma Enterprises",
        "developer": "Ganesh Sharma",
        "current_version": "v1.0"
    }

# CONTACT PAGE ROUTE
@app.get("/contact")
def contact():
    return {
        "email": "ganesh27sharma09@gmail.com",
        "mobile": "90xxx-99xxx",
        "website": "https://ganeshsharma.tech"
    }

