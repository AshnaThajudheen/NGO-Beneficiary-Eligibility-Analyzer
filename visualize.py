import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/beneficiaries.csv")


# Eligibility Distribution
plt.figure(figsize=(8,5))

df["EligibilityStatus"].value_counts().plot(kind="bar")

plt.title("Eligibility Distribution")
plt.xlabel("Eligibility Status")
plt.ylabel("Count")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "screenshots/eligibility_distribution.png",
    bbox_inches="tight"
)
plt.close()

# Education Level Distribution
plt.figure(figsize=(8,5))

df["EducationLevel"].value_counts().plot(kind="bar")

plt.title("Education Level Distribution")
plt.xlabel("Education Level")
plt.ylabel("Count")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "screenshots/education_distribution.png",
    bbox_inches="tight"
)
plt.close()

plt.figure(figsize=(8,5))

plt.hist(df["FamilyIncome"], bins=10)

plt.title("Income Distribution")
plt.xlabel("Family Income")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    "screenshots/income_distribution.png",
    bbox_inches="tight"
)
plt.close()