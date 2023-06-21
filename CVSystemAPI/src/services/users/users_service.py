import bcrypt

from src.core.models.account import Account
from src.core.models.user import User
from src.core.schemas.user import NewUserDto
from src.core.utils.database import DB
from sqlalchemy.orm import Session


def create_new_user(user_data: NewUserDto) -> int:

    with Session(DB.get_instance().engine) as session:
        new_user = User(user_data.first_name, user_data.last_name, user_data.birth_date)

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
