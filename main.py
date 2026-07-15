# importing the modules
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select

# importing the data from the file
from student_information.student_data import STUDENT_DATA
from student_information.semester_data import SEMESTER_1

# importing the schemas
from schemas.student import Student, StudentPartialUpdate

# importing the models
from database.database import Base, engine
from models.student import Student as StudentModel
from database.dependencies import get_db

# creating the database
Base.metadata.create_all(bind = engine)

# initializing the application
app = FastAPI()

# ------------ HOME PAGE ROUTE ------------
@app.get(path = "/")
def home():
    return {
        "message": "Welcome to Student Management API, build by Sharma Enterprises."
    }

# ------------ ABOUT PAGE ROUTE ------------
@app.get("/about")
def about():
    return {
        "project_name": "Student Management System",
        "created_by": "Sharma Enterprises",
        "developer": "Ganesh Sharma",
        "current_version": "v1.0"
    }

# ----------- CONTACT PAGE ROUTE -----------
@app.get("/contact")
def contact():
    return {
        "email": "ganesh27sharma09@gmail.com",
        "mobile": "90xxx-99xxx",
        "website": "https://ganeshsharma.tech"
    }

# ---------- EACH STUDENT INFO PAGE ROUTE ----------
@app.get("/student/{student_id}")
def student_info(student_id: int, db: Session = Depends(get_db)):
    statement = select(StudentModel).where(StudentModel.id == student_id)
    result = db.execute(statement)
    student = result.scalars().first()

    if student is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Student with ID {student_id} not found!")
    
    return student

# --------- QUERY PARAMETER FOR FILTERING BASED ON SEX ---------
@app.get("/students")
def get_students(
    sex: str | None = None,
    latest_qualification: str | None = None,
    db: Session = Depends(get_db)
):
    statement = select(StudentModel)   # the database statement
    
    if sex is not None:
        statement = statement.where(StudentModel.sex == sex)
    
    if latest_qualification is not None:
        statement = statement.where(StudentModel.latest_qualification == latest_qualification)

    result = db.execute(statement)
    students = result.scalars().all()

    return students

# EACH SEMESTER DETAILS PAGE ROUTE
@app.get("/student/{student_id}/semester/{semester}")
def student_semester_detail(student_id: int, semester: int):
    for each_student_marks in SEMESTER_1:
        if student_id == each_student_marks["id"] and semester == 1:
            return student_info(student_id) | each_student_marks

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Marks of Semester {semester} ID {student_id} not found!")

# HELPER FUNCTION FOR FINDING OUT HIGHEST ID AND THEN INCREMENTING IT BY 1
def new_id(DATA):
    HIGHEST_ID = DATA[0]["id"]
    for each_data in DATA:
        if each_data["id"] > HIGHEST_ID:
            HIGHEST_ID = each_data["id"]
    return HIGHEST_ID + 1

# ENDPOINT FOR ADDING A STUDENT'S INFORMATION
@app.post("/student")
def create_student(student: Student, db: Session = Depends(get_db)):
    new_student = {"id": new_id(STUDENT_DATA)} | student.model_dump() # model_dump() converts the Pydantic object to dictionary
    STUDENT_DATA.append(new_student)
    return new_student

# ENDPOINT FOR COMPLETELY REPLACING THE PARTICULAR STUDENT'S INFORMATION
@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student, db: Session = Depends(get_db)):
    for each_student in STUDENT_DATA:
        if each_student["id"] == student_id:
            each_student.clear()
            each_student.update(
                {"id": student_id} | student.model_dump()
            )
            
            return each_student
    
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Student with ID {student_id} not found!")

# ENDPOINT FOR PARTIAL UPDATE OF STUDENT'S INFORMATION
@app.patch("/student/{student_id}")
def partial_update_student(student_id: int, student: StudentPartialUpdate, db: Session = Depends(get_db)):
    for each_student in STUDENT_DATA:
        if each_student["id"] == student_id:
            each_student.update(student.model_dump(exclude_unset = True))

            return each_student
    
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Student with ID {student_id} not found!")

