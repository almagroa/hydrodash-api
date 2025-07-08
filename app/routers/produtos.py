from fastapi import APIRouter
from app.crud import fetch_produtos

router = APIRouter()

@router.get("/produtos", tags=["Metadados"])
def get_produtos():
    return fetch_produtos()