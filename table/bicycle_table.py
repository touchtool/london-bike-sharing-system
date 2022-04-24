from abc import ABC, abstractmethod
import csv
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Float, String, or_, update, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///lend_bicycle.db")
sessionmake = sessionmaker(bind=engine)

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
    end_station_id = Column(Integer)
    start_date = Column(Integer)
    start_month = Column(Integer)
    start_year = Column(Integer)
    start_hour = Column(Integer)
    start_minute = Column(Integer)
    start_station_id = Column(Integer)
    
class Station(Base):
    """Table for stations.csv file"""
    __tablename__ = 'station'
    station_id = Column(Integer, primary_key=True)
    capacity = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    station_name = Column(String(50))

class ICreateTable(ABC):
   @abstractmethod
   def load_data(self):
       pass


class CreateTable(ICreateTable):
    def load_data(file_name, columns, tablename):
        """
        Insert data from csv file to database
        """
        with open(file_name, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            df = pd.DataFrame(data=reader, columns=columns)
        try:
            df.to_sql(tablename, engine, if_exists='append',index=False)
        except:
            print("Somthing Went wrong!!")


class ProxyCreateTable(ICreateTable):
    def __init__(self):
        self.create = CreateTable()

    def load_data(self, file_name, columns, tablename):
        """
        Insert data from csv file to database if the file is not in the table
        """
        inspect = sqlalchemy.inspect(engine)
        if not inspect.has_table(tablename, schema=None):
            CreateTable.load_data(file_name=file_name, columns=columns, tablename=tablename)
        else:
            print(f"this {file_name} already have an information in the database")
