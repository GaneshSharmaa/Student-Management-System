# importing the modules
from pydantic import BaseModel, ConfigDict

# schema for user registeration validation
class UserRegister(BaseModel):
    username: str
    email: str
    password: str

# schema for user response validation
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes = True)

# schema for user login validation
class UserLogin(BaseModel):
    email: str
    password: str

