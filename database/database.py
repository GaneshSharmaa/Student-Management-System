# importing the modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# loading the environment file
load_dotenv()

# reading the environment file
DATABASE_URL = os.getenv("DATABASE_URL")

# creating an engine
engine = create_engine(DATABASE_URL)

# creating a session maker — this would create sessions on every request
SessionLocal = sessionmaker(bind = engine)

