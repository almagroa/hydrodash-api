from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.crud import fetch_climate

router = APIRouter()

@router.get("/clima")
def get_climate(
    bacia_id: int = None,
    start_date: str = None,
    end_date: str = None,
    rodada: str = None,
    produto_id: int = None,
    limit: int = 100
):
    result = fetch_climate(bacia_id, start_date, end_date, rodada, produto_id, limit)
    safe_result = jsonable_encoder(result)
    return JSONResponse(content=safe_result)