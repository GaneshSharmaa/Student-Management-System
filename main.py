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
from models.student import Semester as SemesterModel
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
    statement = select(StudentModel).where(StudentModel.id == student_id)   # query statement (same as SQL)
    result = db.execute(statement)      # executing the query
    student = result.scalars().first()  # storing the result from the database

    # checking if there's no student then raising HTTP exception
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
    statement = select(StudentModel)   # the initial database query statement (same as SQL) to select everything, since it is query parameter
    
    # if sex is given in query parameter then check it
    if sex is not None:
        statement = statement.where(StudentModel.sex == sex)  # updated database query to include sex
    
    # if latest_qualification is given in query parameter then check it
    if latest_qualification is not None:
        statement = statement.where(StudentModel.latest_qualification == latest_qualification)  # updated database query to include latest qualification

    result = db.execute(statement)      # executing the updated database query
    students = result.scalars().all()   # storing the response from the database

    # if no response found from the database then raise HTTP exception
    if students is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Student not found!")

    return students

# EACH SEMESTER DETAILS PAGE ROUTE
@app.get("/student/{student_id}/semester/{semester}")
def student_semester_detail(student_id: int, semester: int, db: Session = Depends(get_db)):
    # database query
    statement = select(SemesterModel).where(SemesterModel.semester == semester and SemesterModel.student_id == student_id)
    # executing the database query and then storing them in a list
    result = db.execute(statement).scalars().all()

    # if nothing is found, raise HTTP exception
    if result is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Student with ID {student_id} in semester {semester} not found!")

    return result

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
    # unpacking the student response body as keyword attributes
    new_student = StudentModel(**student.model_dump())

    db.add(new_student)         # adding the new data
    db.commit()                 # commiting the changes into the database
    db.refresh(new_student)     # refreshing the database so changes are reflected

    return new_student

# ENDPOINT FOR COMPLETELY REPLACING THE PARTICULAR STUDENT'S INFORMATION
@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student, db: Session = Depends(get_db)):
    # database query
    statement = select(StudentModel).where(StudentModel.id == student_id)
    # executing the database query and storing them in a list
    result = db.execute(statement).scalars().first()
    
    # if found nothing, then raise a HTTP exception
    if result is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Student with ID {student_id} not found!")

    # updating the attributes from response body to database attributes
    result.name = student.name
    result.age = student.age
    result.sex = student.sex
    result.latest_qualification = student.latest_qualification

    # commiting and updating the database operations
    db.commit()
    db.refresh(result)
    
    return result

# ENDPOINT FOR PARTIAL UPDATE OF STUDENT'S INFORMATION
@app.patch("/student/{student_id}")
def partial_update_student(student_id: int, student: StudentPartialUpdate, db: Session = Depends(get_db)):
    # database query
    statement = select(StudentModel).where(StudentModel.id == student_id)
    # executing the query and then storing it in an object
    updated_student = db.execute(statement).scalars().first()
    
    # if the requested student is not found, raise HTTP exception
    if updated_student is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Student with ID {student_id} not found!")

    # looping over each attribute from the response body and then updating the database attributes
    for key, value in student.model_dump(exclude_unset = True).items():
        setattr(updated_student, key, value)
    
    # commiting the database operations
    db.commit()
    db.refresh(updated_student)

    return updated_student

