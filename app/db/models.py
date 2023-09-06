from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Slot(Base):
    __tablename__ = "slots"
    
    slot_id = Column(Integer, primary_key=True)
    time = Column(String)
    field_id = Column(Integer, ForeignKey("fields.field_id"))
    price = Column(Float)
    
    playing_field = relationship("Field", back_populates="playtimes")

class Field(Base):
    __tablename__ = "fields"
    
    field_id = Column(Integer, primary_key=True)
    city_id = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    
    playtimes = relationship("Slot", back_populates="playing_field")
    
    
    
    
    
    
    
    