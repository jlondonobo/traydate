from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .models import Field, Slot


def get_slots(db: Session, city_id: str, datetime: str, lat: float, lon: float ):
    distance_expr = func.sqrt(
        func.power(Field.latitude - lat, 2)
        + func.power(Field.longitude - lon, 2)
    )
    stmt = (
        select(Slot)
        .select_from(Slot, Field)
        .where(Field.city_id == city_id)
        .where(Slot.time == datetime)
        .order_by(distance_expr)
    )
    with db as session:
        return session.scalars(stmt).all()
        
    
    
    