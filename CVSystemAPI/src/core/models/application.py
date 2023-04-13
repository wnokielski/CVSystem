from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, MappedColumn

from src.core.models.base import Base


class Application(Base):
    __tablename__ = 'Application'

    id = Column(Integer, primary_key=True)
    status = Column(String(30))
    applicantId = MappedColumn(ForeignKey('User.id'))
    applicant = Relationship('User', back_populates="User")
    workerId = MappedColumn(ForeignKey('User.id'))
    worker = Relationship('User', back_populates='User')
    offerId = MappedColumn(ForeignKey('Offer.id'))
    offer = Relationship('Offer', back_populates='Offer')
    resumeId = MappedColumn(ForeignKey('Resume.id'))
    resume = Relationship('Resume', back_populates='Resume')

    def __Application__(self, status):
        self.status = status
