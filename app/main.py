from fastapi import FastAPI
from app.api.routers import router

app = FastAPI(
    title="Analisador de Currículos com IA",
    description="Recebe PDF, extrai dados e analisa com IA",
    version="1.0.0"
)

app.include_router(router)