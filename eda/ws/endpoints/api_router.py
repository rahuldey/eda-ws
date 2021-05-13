from fastapi import APIRouter
from eda.ws.endpoints import visualization


api_router = APIRouter()

api_router.include_router(
    visualization.router, prefix="/visualization", tags=["visualization"]
)
