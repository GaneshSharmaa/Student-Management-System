from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

from database.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(String(20), nullable = False, unique = True)
    email: Mapped[str] = mapped_column(String(255), nullable = False, unique = True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable = False)

