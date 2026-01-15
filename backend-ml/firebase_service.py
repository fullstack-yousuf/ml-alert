import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://diabetes-monitoring-fyp-default-rtdb.asia-southeast1.firebasedatabase.app"
})

def get_latest_reading():
    ref = db.reference("patients/patient_001/vitals")
    data = ref.get()
    return data


def send_alert(ml_alert):
    alert_ref = db.reference("patients/patient_001/alerts")
    alert_ref.push(ml_alert)
