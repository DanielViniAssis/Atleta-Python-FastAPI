from fastapi import APIRouter
from WorkOutApi.centro_treinamento.controller import router as centro_treinamento
from WorkOutApi.atleta.controller import router as atleta 
from WorkOutApi.categorias.controller import router as categorias 

api_router = APIRouter()
api_router.include_router(atleta, prefix="/atletas", tags=["atletas"])
api_router.include_router(categorias, prefix="/categorias", tags=["categorias"])
api_router.include_router(centro_treinamento, prefix="/centros_treinamento", tags=["centros_treinamento"])
