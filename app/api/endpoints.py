from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/address")
def get_address():
    return {
        "address": {
            "street": "Main Street",
            "city": "FastAPI City",
            "postcode": settings.postcode
        }
    }