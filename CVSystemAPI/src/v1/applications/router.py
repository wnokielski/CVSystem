from fastapi import APIRouter

from src.core.schemas.application import NewApplicationDto
from src.services.applications import applications_service

router = APIRouter()


@router.get("/all")
async def get_all_applications():
    return applications_service.get_all_offers()


@router.get("/{application_id}")
async def get_application_by_id(application_id):
    return applications_service.get_application_by_id(application_id)


@router.get("/byUser/{account_type}/{user_id}")
async def get_applications_by_user(account_type, user_id):
    return applications_service.get_applications_by_user(account_type, user_id)


@router.post("/")
async def create_application(application_details: NewApplicationDto):
    return applications_service.create_application(application_details)


@router.patch("/accept/{application_id}", status_code=204)
async def accept_application(application_id):
    applications_service.accept_application(application_id)


@router.patch("/reject/{application_id}", status_code=204)
async def accept_application(application_id):
    applications_service.reject_application(application_id)

@router.delete("/{application_id}", status_code=204)
async def delete_application(application_id):
    applications_service.delete_application(application_id)
