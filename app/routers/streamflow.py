from fastapi import APIRouter, Query
from typing import Optional
from datetime import date
from app.crud import fetch_streamflow

router = APIRouter()

@router.get("/streamflow")
def get_streamflow(
    bacia_id: Optional[int] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    limit: int = Query(100, le=1000)
):
    return fetch_streamflow(bacia_id, start_date, end_date, limit)
