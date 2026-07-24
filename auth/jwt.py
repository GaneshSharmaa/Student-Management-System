# importing necessary modules
import jwt
from jwt import InvalidTokenError
from fastapi import HTTPException, status
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

# function to generate signed access token
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

# function to decode the signed token and extract useful information
def verify_access_token(token: str) -> str:
    try:
        # decoding the token to get payload
        payload = jwt.decode(jwt = token, key = SECRET_KEY, algorithms = [ALGORITHM])

        # extracting the `sub` claim from the payload
        sub = payload.get("sub")

        # check if claim is not there, raise exception
        if sub is None:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Could not validate credentials"
            )

        return payload

    except InvalidTokenError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Could not validate credentials"
        )

