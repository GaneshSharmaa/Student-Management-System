# importing modules from the pwdlib
from pwdlib import PasswordHash

# creating the password hashing attribute
password_hash = PasswordHash.recommended()

# function to hash the password
def hash_password(password: str) -> str:
    return password_hash.hash(password)

# function to verify the password
def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

