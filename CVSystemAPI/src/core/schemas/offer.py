from pydantic import BaseModel

class NewOfferDto(BaseModel):
    company_name: str
    position: str

class OfferDto(BaseModel):
    id: int
    company_name: str
    position: str