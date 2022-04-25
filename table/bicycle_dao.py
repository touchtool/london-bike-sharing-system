from table.bicycle_load import ProxyCreateTable
from abc import ABC, abstractmethod
from utility import *

create = ProxyCreateTable()
engine = create.get_engine()

class ICreateDAO(ABC):
    @abstractmethod
    def get_query():
        pass

    @abstractmethod
    def get_query_by_id(id: int):
        pass


class CreateStationDao(ICreateDAO):
    def get_query():
        return engine.execute(f"SELECT * FROM {STATION_TABLE_NAME}").fetchall()

    def get_query_by_id(id: int):
        return engine.execute(f"SELECT * FROM {STATION_TABLE_NAME} WHERE station_id={id}").fetchall()

    def update_station_by_id(id: int, capacity=0, latitude=0, longitude=0, station_name=""):
        query = CreateStationDao.get_query_by_id(id)
        if capacity == 0:
            capacity = query[0][1]
        if latitude == 0:
            latitude = query[0][2]
        if longitude == 0:
            longitude = query[0][3]
        if station_name == "":
            station_name = query[0][4]
        engine.execute(f"UPDATE {STATION_TABLE_NAME} SET capacity={capacity}, latitude={latitude}, longitude={longitude}, station_name='{station_name}' WHERE station_id={id}")
        updated_query = engine.execute(f"SELECT * FROM {STATION_TABLE_NAME} WHERE station_id={id}").fetchall()
        return f"Success to update \n {query[0]} \n change to \n {updated_query[0]}"

class CreateJourneyDao(ICreateDAO):
    def get_query():
        return engine.execute(f"SELECT * FROM {JOURNEY_TABLE_NAME}").fetchall()

    def get_query_by_id(id: int):
        return engine.execute(f"SELECT * FROM {JOURNEY_TABLE_NAME} WHERE journey_id={id}").fetchall()

    def update_journey_by_id(id: int, journey_duration=0, end_date=0, end_month=0, end_year=0, end_hour=0, end_minute=0, end_station_id=0, start_date=0, start_month=0, start_year=0, start_hour=0, start_minute=0,	start_station_id=0):
        query = CreateJourneyDao.get_query_by_id(id)
        print(query)
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
        
        engine.execute(f"UPDATE {JOURNEY_TABLE_NAME} SET journey_duration={journey_duration}, \
                        end_date={end_date}, end_month={end_month}, end_year={end_year}, \
                        end_hour={end_hour}, end_minute={end_minute}, end_station_id={end_station_id}, \
                        start_date={start_date}, start_month={start_month}, start_year={start_year}, \
                        start_hour={start_hour}, start_minute={start_minute}, start_station_id={start_station_id}    \
                        WHERE journey_id={id}")
        updated_query = engine.execute(f"SELECT * FROM {JOURNEY_TABLE_NAME} WHERE journey_id={id}").fetchall()
        return f"Success to update \n {query[0]} \n change to \n {updated_query[0]}"
    

class FactoryDAO():
    def __init__(self, creator: ICreateDAO):
        self.creator = creator   

    def find_all(self):
        return self.creator.get_query()
    
    def find_id(self, id):
        return self.creator.get_query_by_id(id)

    def update_station_by_id(self, id, capacity=0, latitude=0, longitude=0, station_name=""):
        print(self.creator.update_station_by_id(id, capacity=capacity, latitude=latitude, longitude=longitude, station_name=station_name))

    def update_journey_by_id(self, id: int, journey_duration=0, end_date=0, end_month=0, end_year=0, end_hour=0, end_minute=0, end_station_id=0, start_date=0, start_month=0, start_year=0, start_hour=0, start_minute=0, start_station_id=0):
        print(self.creator.update_journey_by_id(id, journey_duration, end_date=end_date, end_month=end_month, end_year=end_year, end_hour=end_hour, end_minute=end_minute, end_station_id=end_station_id, start_date=start_date, start_month= start_month, start_year=start_year, start_hour=start_hour, start_minute=start_minute, start_station_id=start_station_id))