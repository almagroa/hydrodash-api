from fastapi import APIRouter, Query, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.crud import fetch_previsao_chuva_rs
from app.auth import verify_token

router = APIRouter()

@router.get("/previsao_chuva_rs", tags=["Previsão Chuva RS"], summary="Consulta dados de previsão de chuva para o RS")
def get_previsao_chuva_rs(
    token: str = Depends(verify_token),
    nome: str = Query(None, description="Nome do local (parcial ou completo)"),
    tipo: str = Query(None, description="Tipo do local (ex: bacia, municipio)"),
    start_date: str = Query(None, description="Data inicial (YYYY-MM-DD)"),
    end_date: str = Query(None, description="Data final (YYYY-MM-DD)"),
    rodada: str = Query(None, description="Data da rodada no formato (YYYY-MM-DD)"),
    produto_id: int = Query(None, description="ID do produto/modelo"),
    limit: int = Query(100, description="Limite de registros retornados")
):
    result = fetch_previsao_chuva_rs(nome, tipo, start_date, end_date, rodada, produto_id, limit)
    safe_result = jsonable_encoder(result)
    return JSONResponse(content=safe_result)
