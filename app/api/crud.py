from datetime import datetime

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.models import TimeSlot


def get_slots(db: Session, city_id: str, time: datetime, lat: float, lon: float):
    distance_expr = func.sqrt(
        func.power(TimeSlot.club_latitude - lat, 2)
        + func.power(TimeSlot.club_longitude - lon, 2)
    )
    stmt = (
        select(TimeSlot)
        .where(TimeSlot.club_city_id == city_id)
        .where(TimeSlot.start_datetime == time)
        .order_by(distance_expr)
    )
    with db as session:
        return session.scalars(stmt).all()
