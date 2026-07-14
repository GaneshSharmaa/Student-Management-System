# importing the local module for session
from database.database import SessionLocal

# creating a dependency
def get_db():
    db = SessionLocal()   # create a new session
    try:
        yield db          # gives the session to the route
    finally:
        db.close()        # closes the session and returns to the connection pool

