from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import database, operations

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{city_id}")
def read_slots(
    city_id: str,
    datetime: str,
    lat: float,
    lon: float,
    db: Session = Depends(get_db),
):
    return operations.get_slots(db, city_id, datetime, lat, lon)
