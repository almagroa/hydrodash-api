from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.crud import fetch_streamflow

router = APIRouter()

@router.get("/streamflow")
def get_streamflow(bacia_id: int = None, start_date: str = None, end_date: str = None, limit: int = 100):
    result = fetch_streamflow(bacia_id, start_date, end_date, limit)
    # Usa encoder para evitar erros com NaN, datetime etc.
    safe_result = jsonable_encoder(result)
    return JSONResponse(content=safe_result)