from fastapi import FastAPI
from anomaly import app as anomaly_app

app = FastAPI()

app.mount("/dashboard", anomaly_app)
