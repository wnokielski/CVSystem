from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import MappedColumn, Relationship

from src.core.models.base import Base


class Account(Base):
    __tablename__ = 'Account'

    id = Column(Integer, primary_key=True)
    user_id = MappedColumn(ForeignKey('User.id'))
    user = Relationship('User', back_populates='account')
    account_type = Column(String(30))
    email_address = Column(String(50))
    password_hash = Column(String(100))

    def __init__(self, us, at, ea, ph):
        self.user = us
        self.account_type = at
        self.email_address = ea
        self.password_hash = ph
