# importing local modules
from database.database import Base

# importing necessary modules
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# `mapped_column` represents database column
# `Mapped` is used for ORM mapping

# database model for student
class Student(Base):
    # table name
    __tablename__ = "students"

    # columns
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50), nullable = False)
    age: Mapped[int] = mapped_column(nullable = False)
    sex: Mapped[str] = mapped_column(String(8), nullable = False)
    latest_qualification: Mapped[str] = mapped_column(String(20), nullable = False)

    # relationship — this lets us navigate between objects
    semester_marks = relationship("SemesterMarks", back_populates = "student")  # back_populates tell that they represent same relationship


# database model for semester data
class SemesterMarks(Base):
    # table name
    __tablename__ = "semester"

    # columns
    semester_id: Mapped[int] = mapped_column(primary_key = True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable = False)
    subject: Mapped[str] = mapped_column(String(25), nullable = False)
    marks: Mapped[int] = mapped_column(Integer, nullable = False)
    semester: Mapped[int] = mapped_column(Integer, nullable = False)

    # relationship — this lets us navigate between objects
    student = relationship("Student", back_populates = "semester_marks")  # back_populates tell that they represent same relationship

