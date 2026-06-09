from sqlalchemy.orm import Session
from .models import Beneficiary

from sqlalchemy import func

def get_all_beneficiaries(db: Session):
    return db.query(Beneficiary).all()

def create_beneficiary(db: Session, beneficiary):
    db_beneficiary = Beneficiary(**beneficiary.dict())
    db.add(db_beneficiary)
    db.commit()
    db.refresh(db_beneficiary)
    return db_beneficiary

def get_beneficiary_by_id(db: Session, beneficiary_id: int):
    return db.query(Beneficiary).filter(
        Beneficiary.id == beneficiary_id
    ).first()

def update_beneficiary(
    db: Session,
    beneficiary_id: int,
    beneficiary_data
):
    beneficiary = db.query(Beneficiary).filter(
        Beneficiary.id == beneficiary_id
    ).first()

    if beneficiary:
        for key, value in beneficiary_data.dict().items():
            setattr(beneficiary, key, value)

        db.commit()
        db.refresh(beneficiary)

    return beneficiary

def delete_beneficiary(
    db: Session,
    beneficiary_id: int
):
    beneficiary = db.query(Beneficiary).filter(
        Beneficiary.id == beneficiary_id
    ).first()

    if beneficiary:
        db.delete(beneficiary)
        db.commit()

    return {"message": "Deleted successfully"}

def get_analytics(db):

    total = db.query(Beneficiary).count()

    eligible = db.query(Beneficiary).filter(
        Beneficiary.eligibility_status == "Eligible"
    ).count()

    not_eligible = db.query(Beneficiary).filter(
        Beneficiary.eligibility_status == "Not Eligible"
    ).count()

    average_income = db.query(
        func.avg(Beneficiary.income)
    ).scalar()

    return {
        "total_applicants": total,
        "eligible": eligible,
        "not_eligible": not_eligible,
        "average_income": round(average_income or 0, 2)
    }