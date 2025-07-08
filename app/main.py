# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import streamflow, clima, bacias, produtos

app = FastAPI(
    title="Hydrodash API",
    description="API para acesso a dados hidrológicos simulados de vazão e precipitação.",
    version="1.0.0"
)

# Permite requisições de qualquer origem (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro dos routers (endpoints)
app.include_router(streamflow.router, tags=["Vazão"])
app.include_router(clima.router, tags=["Clima"])
app.include_router(bacias.router, tags=["Metadados"])
app.include_router(produtos.router, tags=["Metadados"])
