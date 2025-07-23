from fastapi import APIRouter, Query
from app.crud import fetch_bacias
from fastapi import Depends
from app.auth import verify_token

router = APIRouter()

@router.get("/bacias", tags=["Metadados"], summary="Consulta informações sobre as bacias")
def get_bacias(bacia_id: int = Query(None, description="ID da bacia (opcional)"),
               token: str = Depends(verify_token),):
    return fetch_bacias(bacia_id=bacia_id)