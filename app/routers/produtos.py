from fastapi import APIRouter, Query
from app.crud import fetch_produtos

router = APIRouter()

@router.get("/produtos", tags=["Metadados"])
def get_produtos(produto_id: int = Query(None, description="ID do modelo (opcional)")):
    return fetch_produtos(produto_id=produto_id)