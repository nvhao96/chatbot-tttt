import mysql.connector
from mysql.connector import Error

class DBconnector :
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='cafestore',
                                                  user='chatbot',
                                                  password='thaisdang')
        if self.connection.is_connected() :
            self.cursor = self.connection.cursor()
        else:
            self.connection = None
            self.cursor - None

    def fetch(self, query, params=None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insert(self, query, params=None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        self.connection.commit()
    

        