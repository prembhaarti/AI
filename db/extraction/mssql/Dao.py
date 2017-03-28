import pymssql

class Dao:

    server=""
    user=""
    password=""
    dataBase=""

    def __init__(self,server,user,password,dataBase):
        try:
            self.connection=pymssql.connect(server, user, password, dataBase);
            self.cursor=self.connection.cursor(as_dict=True)
            Dao.server=server
            Dao.user=user
            Dao.password=password
            Dao.dataBase=dataBase
        except:
            print("Unable to connect to DB, please check userName, password, database details")

    def createConnectionWithCursor(self):
        self.connection=pymssql.connect(Dao.server, Dao.user, Dao.password, Dao.database);
        self.cursor=self.connection.cursor(as_dict=True)

    def getConnection(self):
        return self.connection

    def getCursor(self):
        return self.cursor

    def getCursorByQuery(self, query):
        self.cursor.execute(query)
        return self.cursor

    def closeConnectionWithCursor(self):
        try:
            self.cursor.close()
            self.connection.close()
        except:
            print("Unable to close Connection")
