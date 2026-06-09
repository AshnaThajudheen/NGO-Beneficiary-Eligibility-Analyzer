# generate_dataset.py

import pandas as pd
import random

names = [
    "Ravi", "Anu", "Rahul", "Meera", "Ajay",
    "Sneha", "Arjun", "Nisha", "Vivek", "Priya",
    "Kiran", "Akhil", "Sanjay", "Asha", "Divya"
]

employment = ["Employed", "Unemployed", "Part-time"]

education = [
    "Diploma",
    "Undergraduate",
    "Graduate",
    "Postgraduate"
]

disability = ["Yes", "No"]

records = []

for i in range(150):

    age = random.randint(18, 60)
    income = random.randint(50000, 800000)
    family_members = random.randint(2, 8)

    emp = random.choice(employment)
    edu = random.choice(education)
    dis = random.choice(disability)

    score = 0

    # Income factor
    if income < 250000:
        score += 3

    # Large family factor
    if family_members >= 5:
        score += 2

    # Disability factor
    if dis == "Yes":
        score += 3

    # Employment factor
    if emp == "Unemployed":
        score += 2

    # Education factor
    if edu in ["Diploma", "Undergraduate"]:
        score += 1

    # Eligibility decision
    if score >= 5:
        eligibility = "Eligible"
    else:
        eligibility = "Not Eligible"

    # Add 10% randomness to make dataset realistic
    if random.random() < 0.10:
        if eligibility == "Eligible":
            eligibility = "Not Eligible"
        else:
            eligibility = "Eligible"

    records.append([
        f"{random.choice(names)} {i}",
        age,
        income,
        family_members,
        emp,
        edu,
        dis,
        eligibility
    ])

df = pd.DataFrame(
    records,
    columns=[
        "ApplicantName",
        "Age",
        "FamilyIncome",
        "FamilyMembers",
        "EmploymentStatus",
        "EducationLevel",
        "DisabilityStatus",
        "EligibilityStatus"
    ]
)

df.to_csv(
    "dataset/beneficiaries.csv",
    index=False
)

print("150 records generated successfully!")