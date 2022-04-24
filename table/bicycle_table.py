from abc import ABC, abstractmethod
import csv
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Float, String, or_, update, select
from sqlalchemy.orm import sessionmaker, Session
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

journey_column = [
            "journey_id",
            "journey_duration",
            "end_date",
            "end_month",
            "end_year",
            "end_hour",
            "end_minute",
            "end_station_id",
            "start_date",
            "start_month",
            "start_year",
            "start_hour",
            "start_minute",
            "start_station_id"
        ]

station_column = [
            "station_id",
            "capacity",
            "latitude",
            "longitude",
            "station_name"
        ]

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
            print("TEST")
        else:
            print(f"this {file_name} already have an information in the database")
        

create = ProxyCreateTable()
create.load_data(file_name="data/journeys.csv", columns=journey_column, tablename=Journey.__tablename__)
create.load_data(file_name="data/stations.csv", columns=station_column, tablename=Station.__tablename__)
# create.load_data(file_name="data/AKC_Breed_Info.csv", columns=akc_breed_column, tablename=AkcBreedInfo.__tablename__)
# create.load_data(file_name="data/dog_intelligence.csv", columns=dog_column, tablename=DogIntelligence.__tablename__)

# session = Session(engine)
# dog_query = select(DogIntelligence)
# result = session.execute(dog_query).all()

# for d in result:
#     print(d[0].id, d[0].breed, d[0].classification, d[0].obey, d[0].reps_lower, d[0].reps_upper)

# print()
# akc_query = select(AkcBreedInfo)
# result = session.execute(akc_query).all()

# for a in result:
#     print(a[0].id, a[0].breed, a[0].height_low_inches, a[0].height_high_inches, a[0].weight_low_lbs, a[0].weight_high_lbs)

# print()

# test = engine.execute("SELECT * FROM dog_intelligence").fetchall()
# print(test)