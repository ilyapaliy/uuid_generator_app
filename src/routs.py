from fastapi import APIRouter
from endpoints import generate_uuid

router = APIRouter()

router.include_router(generate_uuid.router)
