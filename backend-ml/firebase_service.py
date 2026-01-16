import firebase_admin
from firebase_admin import credentials, db
import json
import os
import tempfile

# Read credentials from ENV (GitHub Secret)
firebase_creds = os.environ.get("FIREBASE_CREDENTIALS")

if not firebase_creds:
    raise ValueError("FIREBASE_CREDENTIALS not found in environment variables")

# Write JSON to temp file
with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".json") as f:
    f.write(firebase_creds)
    cred_path = f.name

cred = credentials.Certificate(cred_path)

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://diabetes-monitoring-fyp-default-rtdb.asia-southeast1.firebasedatabase.app"
})

def get_latest_reading():
    ref = db.reference("patients/patient_001/vitals")
    return ref.get()

def send_alert(payload):
    ref = db.reference("patients/patient_001/alerts")
    ref.set(payload)
# import firebase_admin
# from firebase_admin import credentials, db

# cred = credentials.Certificate("serviceAccountKey.json")

# firebase_admin.initialize_app(cred, {
#     "databaseURL": "https://diabetes-monitoring-fyp-default-rtdb.asia-southeast1.firebasedatabase.app"
# })

# def get_latest_reading():
#     ref = db.reference("patients/patient_001/vitals")
#     data = ref.get()
#     return data


# def send_alert(ml_alert):
#     alert_ref = db.reference("patients/patient_001/alerts")
#     alert_ref.push(ml_alert)
