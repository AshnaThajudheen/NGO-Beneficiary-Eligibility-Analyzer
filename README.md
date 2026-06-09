# NGO Beneficiary Eligibility Analyzer

## Project Overview

The NGO Beneficiary Eligibility Analyzer is an AI-powered application developed to help Non-Governmental Organizations (NGOs) identify eligible beneficiaries for various support programs such as educational scholarships, food assistance, medical aid, and skill development initiatives.

The application uses Machine Learning techniques to analyze applicant information and predict whether an applicant is eligible for assistance. It also provides analytics, data visualization, and beneficiary management features through FastAPI and Streamlit.

---

## Objectives

* Automate beneficiary eligibility assessment.
* Reduce manual screening effort.
* Improve decision-making using Machine Learning.
* Provide a user-friendly interface for prediction and analytics.
* Demonstrate AI application development using Python and FastAPI.

---

## Technologies Used

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* Random Forest Classifier

### Frontend

* Streamlit

### Visualization

* Matplotlib

---

## Features

### Beneficiary Management

* Create Beneficiary Records
* View Beneficiary Records
* Update Beneficiary Records
* Delete Beneficiary Records

### Machine Learning Features

* Data Preprocessing
* Label Encoding
* Model Training
* Eligibility Prediction
* Confidence Score Generation

### Analytics Dashboard

* Total Applicants
* Eligible Applicants Count
* Non-Eligible Applicants Count
* Average Family Income

### CSV Upload

* Upload Beneficiary Dataset
* Import Records into SQLite Database

### Data Visualization

* Income Distribution Chart
* Eligibility Distribution Chart
* Education Level Distribution Chart

---

## Dataset Attributes

The dataset contains the following fields:

* Applicant Name
* Age
* Family Income
* Family Members
* Employment Status
* Education Level
* Disability Status
* Eligibility Status

---

## Data Preprocessing

The following preprocessing techniques are applied:

* Missing Value Handling
* Data Cleaning
* Label Encoding

### Why Preprocessing is Important

Machine Learning algorithms work best with clean and structured data. Preprocessing helps improve model accuracy and ensures consistent predictions.

### Consequences of Unclean Data

* Incorrect Predictions
* Reduced Accuracy
* Training Errors
* Poor Model Performance

---

## Machine Learning Model

### Algorithm Used

Random Forest Classifier

### Prediction Output

The model predicts:

* Eligible
* Not Eligible

along with a confidence score.

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* Confusion Matrix

---

## Machine Learning Workflow

Data Collection

↓

Data Cleaning

↓

Feature Engineering

↓

Data Preprocessing

↓

Model Training

↓

Model Evaluation

↓

Prediction API

↓

Beneficiary Eligibility Result

---

## API Endpoints

### Beneficiary Management

GET /beneficiaries

GET /beneficiaries/{id}

POST /beneficiaries

PUT /beneficiaries/{id}

DELETE /beneficiaries/{id}

### Machine Learning

POST /train

POST /predict

### Analytics

GET /analytics

POST /upload-csv

---

## Streamlit Dashboard

The Streamlit dashboard provides:

* Eligibility Prediction Interface
* Confidence Score Display
* Analytics Dashboard
* Dataset Visualizations

Run Streamlit using:

streamlit run streamlit_app.py

Default URL:

http://localhost:8501

---

## Analytics Dashboard

The dashboard displays:

* Total Records
* Eligible Applicants
* Non-Eligible Applicants
* Average Family Income

---

## Visualizations

The project generates:

1. Income Distribution
2. Eligibility Distribution
3. Education Level Distribution

These visualizations help NGOs understand applicant demographics and eligibility trends.

---

## Project Structure

NGO Beneficiary Eligibility Analyzer

├── main.py

├── database.py

├── models.py

├── schemas.py

├── crud.py

├── train.py

├── visualize.py

├── streamlit_app.py

├── beneficiaries.csv

├── requirements.txt

├── README.md

├── income_distribution.png

├── eligibility_distribution.png

└── education_distribution.png

---

## Installation and Setup

### Clone Repository

git clone YOUR_GITHUB_REPOSITORY_URL

cd NGO-Beneficiary-Eligibility-Analyzer

### Create Virtual Environment

python -m venv .venv

### Activate Environment

Windows:

.venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## Running the Application

### Start FastAPI Server

uvicorn main:app --reload

Open Swagger Documentation:

http://127.0.0.1:8000/docs

### Start Streamlit Dashboard

streamlit run streamlit_app.py

Open:

http://localhost:8501

---

## Expected Learning Outcomes

By completing this project, students gain knowledge in:

* Dataset Creation
* Data Cleaning
* Data Preprocessing
* Feature Engineering
* Machine Learning Training
* Classification Models
* Model Evaluation
* FastAPI Development
* REST API Development
* SQLite Database Management
* Streamlit Dashboard Development
* AI Application Development

---

## Future Enhancements

* User Authentication System
* Cloud Deployment
* Email Notifications
* Real-Time Analytics Dashboard
* Advanced Recommendation System
* NGO Management Portal

---

## Conclusion

The NGO Beneficiary Eligibility Analyzer successfully automates beneficiary screening using Machine Learning. The system combines FastAPI, SQLite, Scikit-Learn, and Streamlit to provide prediction, analytics, visualization, and beneficiary management functionalities. This project demonstrates practical AI application development and serves as a foundation for future NGO analytics and decision-support systems.
