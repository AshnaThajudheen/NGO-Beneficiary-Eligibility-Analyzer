from pydantic import BaseModel

class BeneficiaryCreate(BaseModel):
    name: str
    age: int
    income: int
    family_members: int
    employment_status: str
    education_level: str
    disability_status: str
    eligibility_status: str

class BeneficiaryResponse(BeneficiaryCreate):
    id: int

    class Config:
        from_attributes = True

class PredictionRequest(BaseModel):
    age: int
    income: int
    family_members: int
    employment_status: str
    education_level: str
    disability_status: str