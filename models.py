from sqlalchemy import create_engine, Column, Integer, Boolean
from sqlalchemy.orm import declarative_base
from os import getenv
from dotenv import load_dotenv
load_dotenv()
db = create_engine(getenv('SQLALCHEMY_URI'))
Model = declarative_base()

class User(Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    discord_id = Column(Integer, primary_key=True, nullable=False)
    strikes = Column(Integer, default=0)
    muted = Column(Boolean, default=False)