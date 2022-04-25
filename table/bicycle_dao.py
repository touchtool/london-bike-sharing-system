from abc import ABC, abstractmethod
from utility import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table.bicycle_load import ProxyCreateTable

class ICreateDAO(ABC):
    def __init__(self, engine):
        self.engine = engine

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
        return self.engine.execute(f"SELECT * FROM {STATION_TABLE_NAME}").fetchall()

    def get_query_by_id(self, id: int):
        return self.engine.execute(f"SELECT * FROM {STATION_TABLE_NAME} WHERE station_id={id}").fetchall()

    def update_by_id(self, id: int, capacity=0, latitude=0, longitude=0, station_name=""):
        query = CreateStationDao.get_query_by_id(self, id)
        if capacity == 0:
            capacity = query[0][1]
        if latitude == 0:
            latitude = query[0][2]
        if longitude == 0:
            longitude = query[0][3]
        if station_name == "":
            station_name = query[0][4]
        self.engine.execute(f"UPDATE {STATION_TABLE_NAME} SET capacity={capacity}, latitude={latitude}, longitude={longitude}, station_name='{station_name}' WHERE station_id={id}")
        updated_query = self.engine.execute(f"SELECT * FROM {STATION_TABLE_NAME} WHERE station_id={id}").fetchall()
        print(f"Success to update \n {query[0]} \n change to \n {updated_query[0]}")
    
    def __str__(self) -> str:
        return STATION_TABLE_NAME


class CreateJourneyDao(ICreateDAO):
    def get_query(self):
        return self.engine.execute(f"SELECT * FROM {JOURNEY_TABLE_NAME}").fetchall()

    def get_query_by_id(self, id: int):
        return self.engine.execute(f"SELECT * FROM {JOURNEY_TABLE_NAME} WHERE journey_id={id}").fetchall()

    def update_by_id(self, id: int, journey_duration=0, end_date=0, end_month=0, end_year=0, end_hour=0, end_minute=0, end_station_id=0, start_date=0, start_month=0, start_year=0, start_hour=0, start_minute=0,	start_station_id=0):
        query = CreateJourneyDao.get_query_by_id(self, id)
        if journey_duration == 0:
            journey_duration = query[0][1]
        if end_date == 0:
            end_date = query[0][2]
        if end_month == 0:
            end_month = query[0][3]
        if end_year == 0:
            end_year = query[0][4]
        if end_hour == 0:
            end_hour = query[0][5]
        if end_minute == 0:
            end_minute = query[0][6]
        if end_station_id == 0:
            end_station_id = query[0][7]
        if start_date == 0:
            start_date = query[0][8]
        if start_month == 0:
            start_month = query[0][9]
        if start_year == 0:
            start_year = query[0][10]
        if start_hour == 0:
            start_hour = query[0][11]
        if start_minute == 0:
            start_minute = query[0][12]
        if start_station_id == 0:
            start_station_id = query[0][13]
        
        self.engine.execute(f"UPDATE {JOURNEY_TABLE_NAME} SET journey_duration={journey_duration}, \
                        end_date={end_date}, end_month={end_month}, end_year={end_year}, \
                        end_hour={end_hour}, end_minute={end_minute}, end_station_id={end_station_id}, \
                        start_date={start_date}, start_month={start_month}, start_year={start_year}, \
                        start_hour={start_hour}, start_minute={start_minute}, start_station_id={start_station_id}    \
                        WHERE journey_id={id}")
        updated_query = self.engine.execute(f"SELECT * FROM {JOURNEY_TABLE_NAME} WHERE journey_id={id}").fetchall()
        print(f"Success to update \n {query[0]} \n change to \n {updated_query[0]}")
    
    def __str__(self) -> str:
        return JOURNEY_TABLE_NAME

class FactoryDAO():
    def __init__(self, type: str):
        self._engine = create_engine("sqlite:///lend_bicycle.db")
        self._sessionmake = sessionmaker(bind=self._engine)
        self._create_record = ProxyCreateTable(self._engine)
        self.type = type

    def get_create_dao(self):
        if (self.type == JOURNEY_TABLE_NAME):
            return CreateJourneyDao(self._engine)
        elif (self.type == STATION_TABLE_NAME):
            return CreateStationDao(self._engine)

    def load_data(self, file_name, columns, tablename):
        self._create_record.load_data(file_name, columns, tablename)