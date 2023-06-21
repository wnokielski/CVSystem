from fastapi import APIRouter

from src.core.schemas.user import NewUserDto
from src.services.users.users_service import create_new_user

router = APIRouter()

# GET
@router.get("/{user_id}")
async def get_user_by_id(user_id) -> str:
    # TODO implement logic, change returned type
    return "Here will be user with ID " + user_id

# POST

@router.post("/")
async def create_user(user_data: NewUserDto) -> int:
    return create_new_user(user_data)