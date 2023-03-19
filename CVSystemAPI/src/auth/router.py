from fastapi import APIRouter

router = APIRouter()

@router.get("/token")
async def get_auth_token() -> str:
    return "Here will be token"