from fastapi import APIRouter

from src.core.schemas.user import NewUserDto
from src.services.users import users_service

router = APIRouter()


# GET
@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    return users_service.get_user_by_id(user_id)


# POST

@router.post("/")
async def create_user(user_data: NewUserDto) -> int:
    return users_service.create_new_user(user_data)
