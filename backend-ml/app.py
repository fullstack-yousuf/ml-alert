from flask import Flask, jsonify
from firebase_service import get_latest_reading, send_alert
from model import detect
from datetime import datetime

app = Flask(__name__)

@app.route("/check", methods=["GET"])
def check():
    data = get_latest_reading()
    if not data:
        return jsonify({"status": "no data"})

    glucose = data["glucose"]
    heartRate = data["heartRate"]

    is_anomaly = detect(glucose, heartRate)

    if is_anomaly:
        payload = {
            "ml_alert": {
                "glucose": glucose,
                "heartRate": heartRate,
                "timestamp": datetime.now().isoformat(),
                "message": "⚠️testing Anomaly Detected"
            }
        }
    # Pass that payload to your function
        send_alert(payload)

    return jsonify({
        "glucose": glucose,
        "heartRate": heartRate,
        "anomaly": int(is_anomaly),
        
    })

if __name__ == "__main__":
    app.run(debug=True)
