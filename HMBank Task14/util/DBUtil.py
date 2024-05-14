import pyodbc

class DBUtil:
    @staticmethod
    def get_db_conn():
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-MB0Q7BK;DATABASE=HMBank;Trusted_Connection=True')
        return conn
