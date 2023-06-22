from src.core.models.offer import Offer
from src.core.schemas.offer import NewOfferDto
from src.core.utils.database import DB
from sqlalchemy.orm import Session
from sqlalchemy import select


def get_all_offers():
    with Session(DB.get_instance().engine) as session:
        query = select(Offer)
        all_offers = session.execute(query).scalars().all()

    return all_offers


def create_new_offer(offer_details: NewOfferDto):
    with Session(DB.get_instance().engine) as session:
        new_offer = Offer(offer_details.company_name, offer_details.position)

        session.add(new_offer)
        session.flush()
        session.refresh(new_offer)
        new_offer_id = new_offer.id
        session.commit()

    return new_offer_id


def get_offer_by_id(offer_id: int):
    with Session(DB.get_instance().engine) as session:
        query = select(Offer).where(Offer.id == offer_id)
        offer = session.execute(query).scalar()
    return offer
