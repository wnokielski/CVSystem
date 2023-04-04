from fastapi import FastAPI
from src.core.models.user import User
from src.core.models.application import Application
from src.core.models.account import Account
from src.core.models.offer import Offer
from src.core.models.resume import Resume
from src.v1.auth.router import router as auth_router
from src.core.models.base import Base
from src.core.utils.database import DB

engine = DB.get_instance().engine
Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
