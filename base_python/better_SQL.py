import mysql.connector

class SQL_Class:

    def __init__(self):
        self.db = None
        self.cursor = None
        self.tabels = []
        self.database = ''
        self.host = 'localhost'
        self.user = ''
        self.password = ''

    def set_host(self, name:str):
        self.host = name
    def set_login(self, user:str, password:str):
        self.password = password
        self.user = user

    def set_tabels(self, tables:list):
        self.tabels = tables

    def set_database(self, name:str):
        self.database = name

    def login(self,  user:str, password:str, database:str, tables:list, host_name:str = 'localhost'):
        self.host = host_name
        self.password = password
        self.user = user
        self.database = database
        self.tabels = tables

    def connect(self):
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.db.cursor()

    def ifconnected(self):
        if self.cursor == '':
            return False
        else:
            return True

    def basic_read(self, tabels=None, *args, **kwargs):
        if not self.ifconnected():
            raise NotConnected
        if tabels is None:
            tabels = self.tabels
        for x in range(len(tabels)):
            tabels[x] = f'{self.database}.{tabels[x]}'
        tabels_str = ', '.join(tabels)
        if len(args) == 0:
            select = '*'
        else:
            select = ', '.join(args)
        elements = []
        for x in kwargs:
            elements.append(f"{x} = '{kwargs[x]}'")
        elements = ' and '.join(elements)
        Abfrage = f'SELECT {select} FROM {tabels_str} WHERE {elements}'
        Return = self.Execute_SQL_Command(Abfrage)
        return Return


    def basic_write(self, tabels=None, **kwargs):
        if not self.ifconnected():
            raise NotConnected
        if tabels is None:
            tabels = self.tabels
        for x in range(len(tabels)):
            tabels[x] = f'{self.database}.{tabels[x]}'
        tabels_str = tabels[0]
        colums = []
        for x in kwargs:
            colums.append(x)
        values = []
        for x in kwargs:
            values.append(kwargs[x])
        for x in range(len(values)):
            values[x] = f"'{values[x]}'"
        colums = ', '.join(colums)
        values = ', '.join(values)
        Abfrage = f'INSERT INTO {tabels_str} ({colums}) VALUES ({values})'
        self.cursor.execute(Abfrage)
        self.db.commit()

    def Execute_SQL_Command(self, command:str):
        self.cursor.execute(command)
        return self.cursor.fetchall()


class NotConnected(Exception):

    pass

if __name__ == '__main__':
    s = SQL_Class()
    s.login(password='Write_SQL_nowww123!5', user='WRITE', database='homeserver', tables=['cardmarket'])
    s.connect()
    s.set_tabels(['urls'])
    print(s.basic_write(None, url='55', name='33', app='ff'))

