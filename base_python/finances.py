from . import better_SQL as s
from . import dates
import datetime

class finaces:

    def __init__(self, sql:s.SQL_Class):
        self.sql = sql
        self.tables = ["profit", "spendings", "stand"]

    def setup(self):
        #if tabel exists
        pass

    def new_profit(self, number:int, date=None): # id: generated, num, date)
        if date == None:
            date = dates.current()
        self.sql.basic_write(self.tables[0],  profit=number, date=date)

    def new_spending(self, number:int, date=None):
        if date == None:
            date = dates.current()
        self.sql.basic_write(self.tables[0], profit=number, date=date)

    def graph_data(self):
        data_json = {}
        data = self.sql.basic_read()