from fastapi import APIRouter
from app.crud import fetch_bacias

router = APIRouter()

@router.get("/bacias", tags=["Metadados"])
def get_bacias():
    return fetch_bacias()