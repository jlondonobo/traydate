from sqlalchemy import Column, Date, Float, Integer, String

from .database import Base


class TimeSlot(Base):
    __tablename__ = "timeslots"
    
    timeslot_id = Column(String, primary_key=True)
    club_id = Column(Integer)
    club_name = Column(String)
    club_city_id = Column(Integer)
    club_city_name = Column(String)
    club_state_name = Column(String)
    club_image = Column(String)
    club_latitude = Column(Float)
    club_longitude = Column(Float)
    club_members_only_text = Column(String)
    court_id = Column(Integer)
    court_number = Column(Integer)
    min_time_span = Column(Integer)
    max_time_span = Column(Integer)
    date = Column(Date)
    start_time = Column(String)
    start_datetime = Column(Date)
    end_time = Column(String)
    price_info_timespan = Column(Integer)
    price_info_base_amount = Column(Integer)
