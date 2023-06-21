from fastapi import APIRouter

from src.core.schemas.offer import NewOfferDto
from src.services.offers import offers_service

router = APIRouter()


@router.get("/all")
async def get_all_offers():
    return offers_service.get_all_offers()


@router.get("/{offer_id}")
async def get_offer_by_id(offer_id: int):
    return offers_service.get_offer_by_id(offer_id)

@router.post("/")
async def create_offer(offer_details : NewOfferDto):
    return offers_service.create_new_offer(offer_details)
