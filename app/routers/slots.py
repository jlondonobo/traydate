from fastapi import APIRouter

router = APIRouter()

@router.get("/{city_id}")
def fetch_fields(city_id: str):
    return city_id
