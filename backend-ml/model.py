import numpy as np
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.1)

def train():
    X = np.array([
        [100, 80],
        [110, 85],
        [95, 78],
        [300, 150]
    ])
    model.fit(X)

train()

# def detect(glucose, heartRate):
#     prediction = model.predict([[glucose, heartRate]])
#     return prediction[0] == -1

def detect(glucose, heartRate):
    # Convert to numbers safely
    try:
        glucose = float(glucose)
        heartRate = float(heartRate)
    except:
        return False

    # Anomaly conditions
    if glucose < 70 or glucose > 200:
        return True

    if heartRate < 50 or heartRate > 110:
        return True

    return False
