from pydantic import BaseModel
from typing import List, Dict, Optional

class Student(BaseModel):
    name: str
    age: int
    sex: str
    latest_qualification: str

