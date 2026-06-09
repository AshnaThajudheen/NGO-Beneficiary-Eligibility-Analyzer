from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app import models, schemas, crud

from ml.train import train_model
from ml.predict import predict_eligibility

from fastapi import UploadFile, File
import pandas as pd

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="NGO Beneficiary Eligibility Analyzer")

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "NGO Beneficiary Eligibility Analyzer API"}

@app.get("/beneficiaries")
def get_beneficiaries(db: Session = Depends(get_db)):
    return crud.get_all_beneficiaries(db)

@app.post("/beneficiaries")
def create_beneficiary(
    beneficiary: schemas.BeneficiaryCreate,
    db: Session = Depends(get_db)
):
    return crud.create_beneficiary(db, beneficiary)

@app.get("/beneficiaries/{beneficiary_id}")
def get_beneficiary(
    beneficiary_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_beneficiary_by_id(
        db,
        beneficiary_id
    )

@app.put("/beneficiaries/{beneficiary_id}")
def update_beneficiary(
    beneficiary_id: int,
    beneficiary: schemas.BeneficiaryCreate,
    db: Session = Depends(get_db)
):
    return crud.update_beneficiary(
        db,
        beneficiary_id,
        beneficiary
    )

@app.delete("/beneficiaries/{beneficiary_id}")
def delete_beneficiary(
    beneficiary_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_beneficiary(
        db,
        beneficiary_id
    )

@app.post("/train")
def train():

    results = train_model()

    return {
        "message": "Model trained successfully",
        "metrics": results
    }

@app.post("/predict")
def predict(
    request: schemas.PredictionRequest
):

    result = predict_eligibility(
        request.age,
        request.income,
        request.family_members,
        request.employment_status,
        request.education_level,
        request.disability_status
    )

    result["prediction"] = (
        "Eligible"
        if result["prediction"] == 0
        else "Not Eligible"
    )

    return result

@app.get("/analytics")
def analytics(
    db: Session = Depends(get_db)
):
    return crud.get_analytics(db)

@app.post("/upload-csv")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    df = pd.read_csv(file.file)
    # Remove old records first
    db.query(models.Beneficiary).delete()
    db.commit()
    inserted = 0

    for _, row in df.iterrows():

        beneficiary = models.Beneficiary(
            name=row["ApplicantName"],
            age=int(row["Age"]),
            income=int(row["FamilyIncome"]),
            family_members=int(row["FamilyMembers"]),
            employment_status=row["EmploymentStatus"],
            education_level=row["EducationLevel"],
            disability_status=row["DisabilityStatus"],
            eligibility_status=row["EligibilityStatus"]
        )

        db.add(beneficiary)
        inserted += 1

    db.commit()

    return {
        "message": "CSV imported successfully",
        "records_inserted": inserted
    }