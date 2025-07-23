from fastapi import APIRouter, Query
from app.crud import fetch_produtos
from fastapi import Depends
from app.auth import verify_token

router = APIRouter()

@router.get("/produtos", tags=["Metadados"], summary="Consulta informações sobre os modelos climáticos")
def get_produtos(produto_id: int = Query(None, description="ID do modelo (opcional)"),
                 token: str = Depends(verify_token),
                 ):
    return fetch_produtos(produto_id=produto_id)