from sqlite3 import connect
import mysql.connector
import contextlib


class DatabaseManager():
    
    def __init__(self, config: dict) -> None:
        self.configuration = config
        
    
    def __enter__(self):
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, type, value, trace):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        
        


config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'testing'
}

# with DatabaseManager(config) as cursor:
#     _SQL = "SELECT * FROM files WHERE id=269"
    
#     cursor.execute(_SQL)
#     data = cursor.fetchall()
#     print(data)
    
    
    
def foo(fix, *arg, **args):
    print(f'fixed parameter: {fix}')
    print(arg)
    print(args)
    
foo("fix data", "dummy argument", options='config')