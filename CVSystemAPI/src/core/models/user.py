from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Relationship

from src.core.models.base import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    emailAddress = Column(String(50))
    firstName = Column(String(30))
    lastName = Column(String(30))
    birthDate = Column(Date)
    applicant = Relationship('Application', back_populates='Application')
    worker = Relationship('Application', back_populates='Application')
    account = Relationship('Account', back_populates='Account')

    def __User__(self, email, fn, ln):
        self.emailAddress = email
        self.firstName = fn
        self.lastName = ln
