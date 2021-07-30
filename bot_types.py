from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm import declarative_base, sessionmaker

class DbSession:
    def __init__(self, engine):
        self._engine = engine
        self.session_fact = sessionmaker(bind=self._engine)
        self.session = self.session_fact()
        self.Model = declarative_base()
        self.Column = Column
        self.Integer = Integer
        self.Boolean = Boolean
	self.String = String
