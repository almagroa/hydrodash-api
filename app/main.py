from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import streamflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

app.include_router(streamflow.router)

from app.routers import clima
app.include_router(clima.router)
