import joblib
import pandas as pd

model = joblib.load("models/eligibility_model.pkl")

def predict_eligibility(
    age,
    income,
    family_members,
    employment_status,
    education_level,
    disability_status
):

    emp_map = {
        "Employed": 0,
        "Part-time": 1,
        "Unemployed": 2
    }

    edu_map = {
        "Diploma": 0,
        "Graduate": 1,
        "Postgraduate": 2,
        "Undergraduate": 3
    }

    dis_map = {
        "No": 0,
        "Yes": 1
    }

    data = pd.DataFrame([{
        "Age": age,
        "FamilyIncome": income,
        "FamilyMembers": family_members,
        "EmploymentStatus": emp_map[employment_status],
        "EducationLevel": edu_map[education_level],
        "DisabilityStatus": dis_map[disability_status]
    }])

    prediction = model.predict(data)[0]

    confidence = max(
        model.predict_proba(data)[0]
    )

    return {
        "prediction": int(prediction),
        "confidence": round(float(confidence), 2)
    }