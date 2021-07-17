from bot import db
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    discord_id = db.Column(db.Integer, nullable=False)
    strikes = db.Column(db.Integer, default=0)
    muted = db.Column(db.Boolean, default=False)
    guild = db.Column(db.Integer, nullable=False)
        
class CachedUser(Base):
    __tablename__ = "cached_users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=True)
    discriminator = db.Column(db.String(4), nullable=True)