
from fastapi import FastAPI, Query

app = FastAPI()

events = [
    {"date": "2025-04-01", "event": "valve closure", "well": "w1", "feature": "p_pdg", "value": 86},
    {"date": "2025-04-02", "event": "pressure drop", "well": "w1", "feature": "p_pdg", "value": 65},
    {"date": "2025-04-03", "event": "pressure drop", "well": "w1", "feature": "p_pdg", "value": 65},
    {"date": "2025-04-04", "event": "pressure drop", "well": "w1", "feature": "p_pdg", "value": 65},
    # ... فرض کن هزاران ردیف دیگه اینجا هست
]

@app.get("/events")
def get_events(
    page: int = Query(1, ge=1, description="صفحه فعلی"),
    page_size: int = Query(20, ge=1, le=100, description="تعداد رکورد در هر صفحه (پیش فرض 20)")
):
    start = (page - 1) * page_size
    end = start + page_size
    total = len(events)
    return {
        "page": page,
        "page_size": page_size,
        "total": total,
        "items": events[start:end]
    }