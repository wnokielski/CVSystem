from datetime import datetime, timedelta

import bcrypt
import jwt
from basicauth import decode
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.constants import JWT_SECRET, JWT_ALGORITHM
from src.core.models.account import Account
from src.core.models.user import User
from src.core.utils.database import DB


def create_bearer_token(authorization: str):

    # decode user credentials
    email, password = decode(authorization)

    # find user by email
    with Session(DB.get_instance().engine) as session:
        query = select(Account).where(Account.email_address == email)
        user_account = session.execute(query).scalar()

    # check if user exists
    if user_account is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found... Incorrect email?",
        )

    # check if provided password is correct
    is_password_correct = bcrypt.checkpw(password.encode('utf-8'), user_account.password_hash.encode('utf-8'))
    if not is_password_correct:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )

    # create bearer token
    with Session(DB.get_instance().engine) as session:
        query = select(User).where(User.id == user_account.user_id)
        user = session.execute(query).scalar()

    payload = {"user_id": user.id,
               "account_type": user_account.account_type,
               "exp": (datetime.now() + timedelta(days=1))}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {"token": token,
            "user_id": user.id}
