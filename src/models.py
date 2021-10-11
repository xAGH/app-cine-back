import pymysql
from pymysql.err import MySQLError
from src.database import Connection

class Model:

    def __init__(self) -> None:
        self.connection = Connection.open_connection()

    def fetch_one(self, sql: str, as_dict=False, *args):
        try:
            cursor = self.connection.cursor(pymysql.cursors.DictCursor) if as_dict else self.connection.cursor();
            with cursor as cur:
                cur.execute(sql, *args)
                data = cur.fetchone()
                return data
        except MySQLError:
            raise MySQLError
        except Exception:
            raise Exception

    def fetch_all(self, sql: str, as_dict=False, *args):
        try:
            cursor = self.connection.cursor(pymysql.cursors.DictCursor) if as_dict else self.connection.cursor();
            with self.connection.cursor(pymysql.cursors.DictCursor) as cur:
                cur.execute(sql, *args)
                data = cur.fetchall()
                return data
        except MySQLError:
            raise MySQLError
        except Exception:
            raise Exception

    def execute_query(self, sql: str, *args):
        
            with self.connection.cursor() as cur:
                cur.execute(sql, *args)
                self.connection.commit()