from fastapi import APIRouter
from fastapi import Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.crud import fetch_climate
from fastapi import Depends
from app.auth import verify_token

router = APIRouter()

@router.get("/clima", tags=["Clima"], summary="Consulta dados de chuva prevista")
def get_climate(
    token: str = Depends(verify_token),
    bacia_id: int = Query(None, description="ID da bacia hidrográfica"),
    start_date: str = Query(None, description="Data inicial da previsão (YYYY-MM-DD)"),
    end_date: str = Query(None, description="Data final da previsão (YYYY-MM-DD)"),
    rodada: str = Query(None, description="Data da rodada no formato (YYYY-MM-DD)"),
    produto_id: int = Query(None, description="ID do modelo climático"),
    limit: int = Query(100, description="Limite de registros retornados")
):
    result = fetch_climate(bacia_id, start_date, end_date, rodada, produto_id, limit)
    safe_result = jsonable_encoder(result)
    return JSONResponse(content=safe_result)