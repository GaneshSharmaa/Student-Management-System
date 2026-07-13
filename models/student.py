# importing local modules
from database.database import Base

# importing necessary modules
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

# `mapped_column` represents database column
# `Mapped` is used for ORM mapping

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50), nullable = False)
    age: Mapped[int] = mapped_column(nullable = False)
    sex: Mapped[str] = mapped_column(String(8), nullable = False)
    latest_qualification: Mapped[str] = mapped_column(String(20), nullable = False)

