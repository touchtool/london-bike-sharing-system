from abc import ABC, abstractmethod

from utility import *
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import sessionmaker, session
from table.bicycle_load import ProxyCreateTable

class ICreateDAO(ABC):
    def __init__(self, session):
        self.session = session
    
    # @property
    # def commit(self):
    #     return self.commit()

    @abstractmethod
    def get_query(self):
        pass

    @abstractmethod
    def get_query_by_id(self, id: int):
        pass

    @abstractmethod
    def update_by_id(self):
        pass

class CreateStationDao(ICreateDAO):
    def get_query(self):
        statement = select(Station)
        return self.session.execute(statement).fetchall()

    def get_query_by_id(self, id: int):
        statement = select(Station).where(Station.station_id==id)
        return self.session.execute(statement).fetchall()

    def update_by_id(self, id: int, capacity=0, latitude=0, longitude=0, station_name=""):
        query = self.get_query_by_id(id)
        if capacity == 0:
            capacity = query[0][0].capacity
        if latitude == 0:
            latitude = query[0][0].latitude
        if longitude == 0:
            longitude = query[0][0].longitude
        if station_name == "":
            station_name = query[0][0].station_name

        statement = update(Station).where(Station.station_id==id).values(capacity=capacity, latitude=latitude, longitude=longitude, station_name=station_name)
        self.session.execute(statement)
        self.session.commit()
        print(f"Success to update")
    
    def __str__(self) -> str:
        return STATION_TABLE_NAME


class CreateJourneyDao(ICreateDAO):
    def get_query(self):
        statement = select(Journey)
        return self.session.execute(statement).fetchall()

    def get_query_by_id(self, id: int):
        statement = select(Journey).where(Journey.journey_id==id)
        return self.session.execute(statement).fetchall()

    def update_by_id(self, id: int, journey_duration=0, end_date=0, end_month=0, end_year=0, end_hour=0, end_minute=0, end_station_id=0, start_date=0, start_month=0, start_year=0, start_hour=0, start_minute=0,	start_station_id=0):
        query = self.get_query_by_id(id)
        if journey_duration == 0:
            journey_duration = query[0][0].journey_duration
        if end_date == 0:
            end_date = query[0][0].end_date
        if end_month == 0:
            end_month = query[0][0].end_month
        if end_year == 0:
            end_year = query[0][0].end_year
        if end_hour == 0:
            end_hour = query[0][0].end_hour
        if end_minute == 0:
            end_minute = query[0][0].end_minute
        if end_station_id == 0:
            end_station_id = query[0][0].end_station_id
        if start_date == 0:
            start_date = query[0][0].start_date
        if start_month == 0:
            start_month = query[0][0].start_month
        if start_year == 0:
            start_year = query[0][0].start_year
        if start_hour == 0:
            start_hour = query[0][0].start_hour
        if start_minute == 0:
            start_minute = query[0][0].start_minute
        if start_station_id == 0:
            start_station_id = query[0][0].start_station_id
        statement = update(Journey).where(Journey.journey_id==id).values(journey_duration=journey_duration, \
                        end_date=end_date, end_month=end_month, end_year=end_year, \
                        end_hour=end_hour, end_minute=end_minute, end_station_id=end_station_id, \
                        start_date=start_date, start_month=start_month, start_year=start_year, \
                        start_hour=start_hour, start_minute=start_minute, start_station_id=start_station_id)
        self.session.execute(statement)
        self.session.commit()
        print("Success to update")
    
    def __str__(self) -> str:
        return JOURNEY_TABLE_NAME

class FactoryDAO():
    def __init__(self, type: str):
        self._engine = create_engine("sqlite:///lend_bicycle.db")
        self._sessionmake = sessionmaker(bind=self._engine)
        self._create_record = ProxyCreateTable(self._engine)
        self.session = self._sessionmake()
        self.type = type

    def get_create_dao(self):
        if (self.type == JOURNEY_TABLE_NAME):
            return CreateJourneyDao(self.session)
        elif (self.type == STATION_TABLE_NAME):
            return CreateStationDao(self.session)

    def load_data(self, file_name, columns, tablename):
        self._create_record.load_data(file_name, columns, tablename)