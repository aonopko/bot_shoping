import os
from dotenv import load_dotenv

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()

engine = create_engine(os.getenv("SQLALCHEMY_URL"))
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

