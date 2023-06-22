from pydantic import BaseModel

class NewApplicationDto(BaseModel):
    offer_id: int
    applicant_id: int