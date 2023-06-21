from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, MappedColumn

from src.core.models.base import Base


class Application(Base):
    __tablename__ = 'Application'

    id = Column(Integer, primary_key=True)
    status = Column(String(30))
    applicant_id = MappedColumn(ForeignKey('User.id'))
    applicant = Relationship('User', foreign_keys=[applicant_id])
    recruiter_id = MappedColumn(ForeignKey('User.id'))
    recruiter = Relationship('User', foreign_keys=[recruiter_id])
    offer_id = MappedColumn(ForeignKey('Offer.id'))
    # offer = Relationship('Offer', back_populates='Offer')
    resume_id = MappedColumn(ForeignKey('Resume.id'))
    resume = Relationship('Resume', back_populates='application')

    def __init__(self, applicant_id, offer_id):
        self.status = "New"
        self.applicant_id = applicant_id
        # self.recruiter_id = recruiter_id
        self.offer_id = offer_id
