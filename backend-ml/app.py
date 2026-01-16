from firebase_service import get_latest_reading, send_alert
from model import detect
from datetime import datetime

def run():
    data = get_latest_reading()
    if not data:
        print("No data found")
        return

    glucose = data["glucose"]
    heartRate = data["heartRate"]

    is_anomaly = detect(glucose, heartRate)

    if is_anomaly:
        payload = {
            "ml_alert": {
                "glucose": glucose,
                "heartRate": heartRate,
                "timestamp": datetime.now().isoformat(),
                "message": "⚠️ Anomaly Detected"
            }
        }
        send_alert(payload)

    print({
        "glucose": glucose,
        "heartRate": heartRate,
        "anomaly": int(is_anomaly)
    })

if __name__ == "__main__":
    run()

