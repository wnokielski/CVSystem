from src.core.models.account import Account
from src.core.models.application import Application
from src.core.schemas.application import NewApplicationDto
from src.core.utils.database import DB
from sqlalchemy.orm import Session
from sqlalchemy import select, func, delete


def get_all_applications():
    with Session(DB.get_instance().engine) as session:
        query = select(Application)
        all_applications = session.execute(query).scalars().all()

    return all_applications


def get_application_by_id(application_id: int):
    with Session(DB.get_instance().engine) as session:
        query = select(Application).where(Application.id == application_id)
        application = session.execute(query).scalar()

    return application


def get_applications_by_user(account_type, user_id):
    with Session(DB.get_instance().engine) as session:
        query = select(Application)

        if account_type == "applicant":
            query = query.where(Application.applicant_id == user_id)
        else:
            query = select(Application).where(Application.recruiter_id == user_id)

        applications = session.execute(query).scalars().all()

    return applications


def create_application(application_details: NewApplicationDto):
    with Session(DB.get_instance().engine) as session:
        application = Application(application_details.applicant_id, application_details.offer_id)
        select_recruiter(application)

        session.add(application)
        session.flush()
        session.refresh(application)
        application_id = application.id
        session.commit()

    return application_id


def accept_application(application_id):
    with Session(DB.get_instance().engine) as session:
        # find application
        query = select(Application).where(Application.id == application_id)
        application = session.execute(query).scalar()

        # change status
        application.status = "Accepted"

        # commit to DB
        session.add(application)
        session.commit()


def reject_application(application_id):
    with Session(DB.get_instance().engine) as session:
        # find application
        query = select(Application).where(Application.id == application_id)
        application = session.execute(query).scalar()

        # change status
        application.status = "Rejected"

        # commit to DB
        session.add(application)
        session.commit()


def delete_application(application_id):
    with Session(DB.get_instance().engine) as session:
        query = delete(Application).where(Application.id == application_id)
        session.execute(query)


def select_recruiter(application: Application):
    with Session(DB.get_instance().engine) as session:
        # get random recruiter
        query = select(Account).where(Account.account_type == "recruiter").order_by(func.random()).limit(1)
        recruiter = session.execute(query).scalar()
        application.recruiter_id = recruiter.user_id

    return application
