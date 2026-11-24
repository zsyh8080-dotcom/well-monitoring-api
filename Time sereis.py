
from fastapi import FastAPI, Query
from typing import List, Dict, Optional
from datetime import datetime, timedelta

app = FastAPI(title="Well Time Series API")

fake_data = {
    "2025-01-01": {"p_pdg": 70, "p_tpt": 40, "t_tpt": 30},
    "2025-01-02": {"p_pdg": 68, "p_tpt": 41, "t_tpt": 29},
    "2025-01-03": {"p_pdg": 72, "p_tpt": 39, "t_tpt": 31},
    "2025-01-04": {"p_pdg": 75, "p_tpt": 42, "t_tpt": 32},
}

@app.get("/wells/{well_id}/timeseries")
def get_timeseries(
    well_id: int,
    granularity: str = Query("day", enum=["hour", "day", "month"]),
    from_date: Optional[str] = Query(None, description="YYYY-MM-DD"),
    to_date: Optional[str] = Query(None, description="YYYY-MM-DD"),
    metrics: Optional[str] = Query(None, description="comma separated list of metrics")
):
    """
    API سری زمانی برای هر چاه
    - granularity = hour | day | month
    - from_date / to_date = بازه تاریخی
    - metrics = مثلا 'p_pdg,p_tpt,t_tpt'
    """

    selected_metrics = metrics.split(",") if metrics else None

    points = []
    for date_str, values in fake_data.items():
        if from_date and date_str < from_date:
            continue
        if to_date and date_str > to_date:
            continue

        if selected_metrics:
            values = {k: v for k, v in values.items() if k in selected_metrics}

        points.append({
            "name": date_str,
            "value": values
        })

    return {
        "well_id": well_id,
        "granularity": granularity,
        "points": points
    }