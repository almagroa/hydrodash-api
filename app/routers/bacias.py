from fastapi import APIRouter, Query
from app.crud import fetch_bacias

router = APIRouter()

@router.get("/bacias", tags=["Metadados"], summary="Consulta informações sobre as bacias")
def get_bacias(bacia_id: int = Query(None, description="ID da bacia (opcional)")):
    return fetch_bacias(bacia_id=bacia_id)