from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Journey(Base):
    """Table for jporneys.csv file"""
    __tablename__ = 'journey'
    journey_id = Column(Integer, primary_key=True)
    journey_duration = Column(Integer)
    end_date = Column(Integer)
    end_month = Column(Integer)
    end_year = Column(Integer)
    end_hour = Column(Integer)
    end_minute = Column(Integer)
    end_station_id = Column(Integer, ForeignKey('station.station_id'))
    start_date = Column(Integer)
    start_month = Column(Integer)
    start_year = Column(Integer)
    start_hour = Column(Integer)
    start_minute = Column(Integer)
    start_station_id = Column(Integer, ForeignKey('station.station_id'))
