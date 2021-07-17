from sqlalchemy.engine import create_engine
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os
import dotenv
dotenv.load_dotenv()
engine = create_engine(os.getenv('SQLALCHEMY_URI'))
session = sessionmaker(bind=engine)()
Model = declarative_base()
class User(Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    discord_id = Column(Integer, nullable=False)
    strikes = Column(Integer, default=0)
    muted = Column(Boolean, default=False)
    guild = Column(Integer, nullable=False)
        
class CachedUser(Model):
    __tablename__ = "cached_users"
    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=True)
    discriminator = Column(String(4), nullable=True)