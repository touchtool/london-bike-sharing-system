from models.journey_model import Journey
from models.station_model import Station
PATH_JOURNEY_CSV = "data/journeys.csv"
PATH_STATION_CSV = "data/stations.csv"

JOURNEY_TABLE_NAME = Journey.__tablename__
STATION_TABLE_NAME = Station.__tablename__

STATION_TABLE = Station
JOURNEY_TABLE = Journey

JOURNEY_COLUMN = [
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

STATION_COLUMN = [
            "station_id",
            "capacity",
            "latitude",
            "longitude",
            "station_name"
        ]