from datetime import datetime

import bcrypt
from fastapi import HTTPException
from sqlalchemy import select
from starlette import status

from src.core.models.account import Account
from src.core.models.user import User
from src.core.schemas.user import NewUserDto
from src.core.utils.database import DB
from sqlalchemy.orm import Session


def create_new_user(user_data: NewUserDto) -> int:

    with Session(DB.get_instance().engine) as session:

        query = select(Account).where(Account.email_address == user_data.email_address)
        user_account = session.execute(query).scalar()

        # check if user already exists
        if user_account is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this e-mail already exists!",
            )

        # convert date from string to timestamp
        date = datetime.strptime(user_data.birth_date, '%Y-%m-%d').isoformat()

        new_user = User(user_data.first_name, user_data.last_name, date)

        # hash user password
        bytes = user_data.password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)

        new_account = Account(new_user, user_data.account_type, user_data.email_address, hash)

        session.add_all([new_account, new_user])
        session.flush()
        session.refresh(new_account)
        new_account_id = new_account.id
        session.commit()
    return new_account_id

def get_user_by_id(user_id: int):
    with Session(DB.get_instance().engine) as session:
        query = select(User).where(User.id == user_id)
        user = session.execute(query).scalar()

        query = select(Account).where(Account.user_id == user_id)
        account = session.execute(query).scalar()
    return {"first_name": user.first_name,
            "last_name": user.last_name,
            "email_address": account.email_address,
            "account_type": account.account_type}
