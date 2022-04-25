from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Station(Base):
    """Table for stations.csv file"""
    __tablename__ = 'station'
    station_id = Column(Integer, primary_key=True)
    capacity = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    station_name = Column(String(50))