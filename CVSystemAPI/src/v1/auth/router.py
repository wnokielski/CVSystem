from typing import Union

from fastapi import APIRouter, Header

from src.services.auth import auth_service

router = APIRouter()

@router.get("/token")
async def get_auth_token(authorization: Union[str, None] = Header(default=None)):
    return auth_service.create_bearer_token(authorization)