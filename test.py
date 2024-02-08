import base_python
from dotenv import load_dotenv
load_dotenv()
import os


sql = base_python.better_SQL.SQL_Class()
sql.login(password=os.environ['pasw_READ'], user=os.environ['pasw_READ'], database='homeserver', tables=['homeserver'])
sql.basic_write()