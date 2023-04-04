from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship

from src.core.models.base import Base


class Offer(Base):
    __tablename__ = 'Offer'

    id = Column(Integer, primary_key=True)
    companyName = Column(String(30))
    position = Column(String(50))
    application = Relationship('Application', back_populates='Application')
