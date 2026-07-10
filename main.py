# importing the modules
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# importing the data from the file
from student_information.student_data import STUDENT_DATA
from student_information.semester_data import SEMESTER_1

# importing the schemas
from schemas.student import Student

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

# QUERY PARAMETER FOR FILTERING BASED ON SEX
@app.get("/students")
def filter_sex(sex: str | None = None, latest_qualification: str | None = None):
    filtered_students = []

    for each_student in STUDENT_DATA:
        if sex is not None and each_student["sex"] != sex:
            continue

        if (latest_qualification is not None and each_student["latest_qualification"] != latest_qualification):
            continue

        filtered_students.append(each_student)

    return filtered_students

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

def highest_id(DATA):
    HIGHEST_ID = DATA[0]["id"]
    for each_data in DATA:
        if each_data["id"] > HIGHEST_ID:
            HIGHEST_ID = each_data["id"]
    return HIGHEST_ID + 1


# ENDPOINT FOR ADDING A STUDENT'S INFORMATION
@app.post("/student")
def create_student(student: Student):
    new_student = {"id": highest_id(STUDENT_DATA)} | student.model_dump() # model_dump() converts the Pydantic object to dictionary
    STUDENT_DATA.append(new_student)
    return new_student

@app.put("/student/{student_id}")
def update_student(student: Student, student_id: int):
    for each_student in STUDENT_DATA:
        if student_id == each_student["id"]:
            each_student = {("id": student_id) | (student.model_dump())}
        else:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Student not found!")
    
    return student

