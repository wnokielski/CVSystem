from fastapi import FastAPI
from src.v1.auth.router import router as auth_router
from src.core.models.base import Base
from src.core.utils.database import DB

engine = DB.get_instance().engine
Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
