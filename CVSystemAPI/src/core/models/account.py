from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import MappedColumn, Relationship

from src.core.models.base import Base


class Account(Base):
    __tablename__ = 'Account'

    id = Column(Integer, primary_key=True)
    userId = MappedColumn(ForeignKey('User.id'))
    user = Relationship('User', back_populates='User')
    accountType = Column(String(30))
    login = Column(String(30))
    passwordHash = Column(String(100))
