from sqlalchemy import Column, Integer, String
from .database import Base

class Beneficiary(Base):
    __tablename__ = "beneficiaries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    income = Column(Integer)
    family_members = Column(Integer)
    employment_status = Column(String)
    education_level = Column(String)
    disability_status = Column(String)
    eligibility_status = Column(String)