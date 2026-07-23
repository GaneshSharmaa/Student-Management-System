from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Optional

class Student(BaseModel):
    name: str
    age: int
    sex: str
    latest_qualification: str

class StudentPartialUpdate(BaseModel):
    name: str | None = None     # this None = None, means it has a default value None
    age: int | None = None
    sex: str | None = None
    latest_qualification: str | None = None

class SemesterMarkResponse(BaseModel):
    subject: str
    marks: int

    model_config = ConfigDict(from_attributes = True)

class StudentResponse(Student):
    id: int
    semester_marks: List[SemesterMarkResponse]

    model_config = ConfigDict(from_attributes = True)

