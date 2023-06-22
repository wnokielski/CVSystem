from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Relationship

from src.core.models.base import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    birth_date = Column(Date)
    account = Relationship('Account', back_populates='user')

    def __init__(self, fn, ln, bd):
        self.first_name = fn
        self.last_name = ln
        self.birth_date = bd
