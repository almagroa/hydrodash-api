from fastapi import APIRouter, Query
from app.crud import fetch_produtos

router = APIRouter()

@router.get("/produtos", tags=["Metadados"], summary="Consulta informações sobre os modelos climáticos")
def get_produtos(produto_id: int = Query(None, description="ID do modelo (opcional)")):
    return fetch_produtos(produto_id=produto_id)