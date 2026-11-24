
from fastapi import FastAPI
import random

app = FastAPI(title="Anomaly Pie Chart API")

ANOMALY_COLORS = {
    "normal": "#4caf50",
    "flow instability": "#2196f3",
    "pressure anomaly": "#f44336",
    "temperature anomaly": "#ff9800",
    "fluid level anomaly": "#9c27b0",
    "viscosity anomaly": "#3f51b5",
    "gas anomaly": "#00bcd4",
    "chemical composition": "#009688",
    "flow rate": "#795548"
}

@app.get("/dashboard/anomalies/pie")
def get_anomaly_pie():
    items = []
    for name, color in ANOMALY_COLORS.items():
        value = random.randint(0, 50)  # داده رندوم
        items.append({
            "name": name,
            "value": value,
            "color": color
        })

    return {"items": items}