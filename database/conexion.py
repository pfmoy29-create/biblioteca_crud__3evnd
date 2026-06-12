import psycopg2

class Conexion:

    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(host="localhost", database= "biblioteca_3aevnd",user="postgres," password="123456",port="5432")