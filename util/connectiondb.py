import mysql.connector

user = 'root'
password = ''
host = '127.0.0.1'

class Database:
    def __init__(self):
        self.cnx = mysql.connector.connect(user=user, password=password, host=host)

    def executar(self, comando, parametros):
        cs = self.cnx.cursor()
        cs.execute(comando, parametros)
        self.cnx.commit()
        cs.close()
        return True

class SQL:
   def __init__(self, esquema):
       self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=esquema)

   def executar(self, comando, parametros):
       cs = self.cnx.cursor()
       cs.execute(comando, parametros)
       self.cnx.commit()
       cs.close()
       return True

   def consultar(self, comando, parametros):
       cs = self.cnx.cursor()
       cs.execute(comando, parametros)
       return cs

   def __del__(self):
       self.cnx.close()