from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import MappedColumn, Relationship

from src.core.models.base import Base


class Resume(Base):
    __tablename__ = 'Resume'

    id = Column(Integer, primary_key=True)
    # applicationId = MappedColumn(ForeignKey('Application.id'))
    application = Relationship('Application', back_populates='resume')
    originalFilename = Column(String(100))
    fileUrl = Column(String(255))
