from sqlalchemy.engine import create_engine
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os
import dotenv
dotenv.load_dotenv()
engine = create_engine(os.getenv('SQLALCHEMY_URI'))
session = sessionmaker(bind=engine)()
Model = declarative_base()