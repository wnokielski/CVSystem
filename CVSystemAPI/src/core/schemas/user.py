from datetime import datetime

from pydantic import BaseModel

class NewUserDto(BaseModel):
    email_address: str
    first_name: str
    last_name: str
    birth_date: str
    account_type: str
    password: str
