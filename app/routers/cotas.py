from fastapi import APIRouter, Query, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.crud import fetch_cotas, fetch_cotas_obs, fetch_bacias_cotas
from app.auth import verify_token

router = APIRouter()

@router.get("/bacias_cotas", tags=["Cotas"], summary="Consulta informações sobre as bacias com medição de cota")
def get_bacias_cotas(bacia_id: int = Query(None, description="ID da bacia (opcional)"),
                     token: str = Depends(verify_token)):
    return fetch_bacias_cotas(bacia_id=bacia_id)

@router.get("/cotas", tags=["Cotas"], summary="Consulta dados de cota prevista")
def get_cotas(
    token: str = Depends(verify_token),
    bacia_id: int = Query(None, description="ID da bacia hidrográfica"),
    start_date: str = Query(None, description="Data inicial da previsão (YYYY-MM-DD)"),
    end_date: str = Query(None, description="Data final da previsão (YYYY-MM-DD)"),
    rodada: str = Query(None, description="Data da rodada no formato (YYYY-MM-DD)"),
    produto_id: int = Query(None, description="ID do modelo climático"),
    limit: int = Query(100, description="Limite de registros retornados")
):
    result = fetch_cotas(bacia_id, start_date, end_date, rodada, produto_id, limit)
    safe_result = jsonable_encoder(result)
    return JSONResponse(content=safe_result)

@router.get("/cotas_observadas", tags=["Cotas"], summary="Consulta dados de cota observada")
def get_cotas_obs(
    token: str = Depends(verify_token),
    bacia_id: int = Query(None, description="ID da bacia hidrográfica"),
    start_date: str = Query(None, description="Data inicial da observação (YYYY-MM-DD)"),
    end_date: str = Query(None, description="Data final da observação (YYYY-MM-DD)"),
    limit: int = Query(100, description="Limite de registros retornados")
):
    result = fetch_cotas_obs(bacia_id, start_date, end_date, limit)
    safe_result = jsonable_encoder(result)
    return JSONResponse(content=safe_result)
