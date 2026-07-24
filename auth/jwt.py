# importing necessary modules
import jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta, timezone

# loading the environment variables
load_dotenv()

# all the constant values
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# check to handle cases where environment is empty
if SECRET_KEY is None:
    raise ValueError("SECRET_KEY environment variable not set.")

def create_access_token(data: dict) -> str:
    # making a copy of the data dictionary
    to_encode = data.copy()

    # calculating the expiry of the token
    expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)

    # changing the `exp` claim to expiry that we calculated
    to_encode["exp"] = expire

    # encoding the token
    jwt_string = jwt.encode(payload = to_encode, key = SECRET_KEY, algorithm = ALGORITHM)

    return jwt_string

