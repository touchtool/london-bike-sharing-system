from abc import ABC, abstractmethod
import csv
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ICreateTable(ABC):
   @abstractmethod
   def load_data(self):
       pass


class CreateTable(ICreateTable):
    def load_data(file_name, columns, tablename, engine):
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
        self._engine = create_engine("sqlite:///lend_bicycle.db")
        self._sessionmake = sessionmaker(bind=self._engine)

    def load_data(self, file_name, columns, tablename):
        """
        Insert data from csv file to database if the file is not in the table
        """
        inspect = sqlalchemy.inspect(self._engine)
        if not inspect.has_table(tablename, schema=None):
            CreateTable.load_data(file_name=file_name, columns=columns, tablename=tablename, engine=self._engine)
        else:
            print(f"this {file_name} already have an information in the database")

    def get_engine(self):
        return self._engine
