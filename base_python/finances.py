from . import better_SQL as s
from . import dates
import datetime

class finaces:

    def __init__(self, sql:s.SQL_Class):
        self.sql = sql
        self.tables = ["profit", "spending", "stand"]

    def setup(self):
        #if tabel exists
        pass

    def new_profit(self, number:int, type:str, date=None): # id: generated, num, date)
        if date == None:
            date = dates.current()
        self.sql.basic_write(self.tables[0],  profit=number, type=type, date=date)

    def new_spending(self, number:int, type:str, date=None):
        if date == None:
            date = dates.current()
        self.sql.basic_write(self.tables[0], profit=number, type=type, date=date)

    def read_data(self):
        data = self.sql.basic_read([self.tables[0], self.tables[1]])
        return data

class process_data:

    def __init__(self, data:list):
        pass

class Graph:

    def __init__(self):
        pass