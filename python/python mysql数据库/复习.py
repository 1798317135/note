import mysql.connector

class Mysql:
    def __enter__(self):
        mydb = mysql.connector.connect(
            user = 'root',
            password = '123456',
            host = 'localhost',
            database = 'test1',
            charset = 'utf8',
        )
        self.db = mydb
        return self.db

    def __exit__(self,exc_type,exc_value,ext_tb):
        print(self,exc_type,exc_value,ext_tb)
        import traceback
        if traceback.extract_tb(ext_tb):
            print(traceback.extract_tb(ext_tb))
            self.db.rollback()
        return True

with Mysql() as mydb:
    print(mydb.cursor())
    
