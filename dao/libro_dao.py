#DAO: Data Access Object
#Es una clase que se encarga de acceder
#a la base dedstos y relizar las operaciones

from database.conexion import Conexion
from Models.libro import Libro

class LibroDAO:
    #Select * from libros
    def obtener_libros(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        
        #Ejecuta la consulta
        cursor.execute("Select * FROM libro")
        #Obtiene los resultados
        registros = cursor.fetchall()

        #Crear una lista de clase libro
        libros=[]
        for  registros in registros:
            libro = Libro(
                id=registros[0],
                titulo=registros[1],
                autor=registros[2],
                isbn=registros[1],
                disponible=registros[4]
            )
        
            libros.append(libro)
        #Cerrar la conexion
        cursor.close()
        conexion.close()
       #Conexion.close()
        return libros

    #Insertar
    def insertar(self,libro):
        Conexion = Conexion.obtener_conexion()
        cursor = Conexion.cursor()

        sql= """
        INSERT INTO libro(titulo,autor,isbn,disponible)
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(sql,(
            libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible
        ))

        Conexion.commit()
        cursor.close()
        Conexion.close()

    def actualizar(self,libro):
        Conexion = Conexion.obtener_conexion()
        cursor = Conexion.cursor()

        sql= """
              UPDATE libro
              SET titulo = %s, autor=%x,
              isbn = %s, disponible = %s
              WHERE id = %s
        """

        cursor.execute(sql,(
            libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible,
            libro.id
        ))

        Conexion.commit()
        cursor.close()
        Conexion.close()

    def eliminar (self,id):
        Conexion = Conexion.obetner_conexion()
        cursor = Conexion.cursor()

        cursor.execute("DELETE FROM libro WHERE id = %s",
            (id))
        Conexion.commit()
        cursor.close()
        Conexion.close()