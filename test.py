import os
import random
import base_python
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

#sql = base_python.better_SQL.SQL_Class()
#sql.login(user=os.environ['user_write'], password=os.environ['pasw_write'], database='testdatabase', tables=[])
#sql.connect()
#f = base_python.finances.finances.finaces(sql)
#data = f.read_data()




from datetime import datetime

def sort_list_of_lists(list_of_lists):
    # Verwenden Sie die sort-Methode mit einem benutzerdefinierten Schlüssel, um die Liste zu sortieren
    sorted_list = sorted(list_of_lists, key=lambda x: x[-1])
    return sorted_list


# Beispielaufruf
list_of_lists = [
    [[1, sum], datetime(2023, 1, 15)],
    [[3, sum], datetime(2023, 2, 28)],
    [[8, sum], datetime(2023, 1, 3)],
    [[10, sum], datetime(2023, 2, 8)],
    [[11, sum], datetime(2023, 3, 7)],
    [[9, sum], datetime(2023, 4, 1)],
    [[2, sum], datetime(2023, 4, 4)],
]

list_of_lists2 = [
    [[1, sum], datetime(2023, 1, 15)],
    [[3, sum], datetime(2023, 2, 28)],
    [[8, sum], datetime(2023, 1, 3)],
    [[9, sum], datetime(2023, 4, 1)],
    [[2, sum], datetime(2023, 4, 4)],
]

d = base_python.data.data.process_data({'time' : relativedelta(months=1)}, a=list_of_lists, b=list_of_lists2)
labels, data = d.get()

g = base_python.data.graph.graph(labels, data)
g.basic_view()
