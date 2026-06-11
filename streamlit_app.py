import streamlit as st
import requests

API_URL = "https://ngo-beneficiary-eligibility-analyzer.onrender.com"

st.title("NGO Beneficiary Eligibility Analyzer")

# =========================
# Prediction Section
# =========================

st.header("Eligibility Prediction")

age = st.number_input("Age", min_value=0)
income = st.number_input("Family Income", min_value=0)
family_members = st.number_input("Family Members", min_value=1)

employment_status = st.selectbox(
    "Employment Status",
    ["Employed", "Unemployed", "Part-time"]
)

education_level = st.selectbox(
    "Education Level",
    ["Diploma", "Undergraduate", "Graduate", "Postgraduate"]
)

disability_status = st.selectbox(
    "Disability Status",
    ["Yes", "No"]
)

if st.button("Predict"):

    data = {
        "age": age,
        "income": income,
        "family_members": family_members,
        "employment_status": employment_status,
        "education_level": education_level,
        "disability_status": disability_status
    }

    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=data
        )

        result = response.json()

        st.success(
            f"Prediction: {result['prediction']}"
        )

        st.info(
            f"Confidence: {result['confidence'] * 100:.2f}%"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")



st.subheader("Income Distribution")
st.image(
    "screenshots/income_distribution.png",
    use_container_width=True
)

st.subheader("Eligibility Distribution")
st.image(
    "screenshots/eligibility_distribution.png",
    use_container_width=True
)

st.subheader("Education Level Distribution")
st.image(
    "screenshots/education_distribution.png",
    use_container_width=True
)
