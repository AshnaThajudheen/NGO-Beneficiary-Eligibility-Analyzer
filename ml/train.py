import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix
)

def train_model():

    df = pd.read_csv("dataset/beneficiaries.csv")

    le_emp = LabelEncoder()
    le_edu = LabelEncoder()
    le_dis = LabelEncoder()
    le_target = LabelEncoder()

    df["EmploymentStatus"] = le_emp.fit_transform(df["EmploymentStatus"])
    df["EducationLevel"] = le_edu.fit_transform(df["EducationLevel"])
    df["DisabilityStatus"] = le_dis.fit_transform(df["DisabilityStatus"])
    df["EligibilityStatus"] = le_target.fit_transform(df["EligibilityStatus"])

    X = df.drop(
        ["ApplicantName", "EligibilityStatus"],
        axis=1
    )

    y = df["EligibilityStatus"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)

    cm = confusion_matrix(y_test, predictions)

    joblib.dump(
        model,
        "models/eligibility_model.pkl"
    )

    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "confusion_matrix": cm.tolist()
    }