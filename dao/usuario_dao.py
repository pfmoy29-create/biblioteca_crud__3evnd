from database.conexion import Conexion
from Models.usuarios import Usuario

class UsuarioDAO:

    #SELECT * FROM usuario
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM vista_usuario")
        registros = cursor.fetchall()

        usuarios = []
        for registro in registros : 
            usuario = Usuario(
                id  = registro[0],
                nombre = registro[1],
                matricula = registro[2],
                carrera = registro[3],
                correo = registro[4],
                activo = registro[5]
            )
            usuarios.append(usuario)
        cursor.close()
        conexion.close()
        return usuarios
    
    
    # INSERT
    def insertar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO usuario(id, nombre, matricula, carrera, correo, activo)
        VALUES(%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            usuario.id,
            usuario.nombre, 
            usuario.matricula, 
            usuario.carrera,
            usuario.correo,
            usuario.activo
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # UPDATE
    def actualizar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuario
        SET nombre = %s, carrera = %s, correo = %s, activo = %s
        WHERE id = %s
        """

        cursor.execute(sql, (
                       usuario.nombre,
                       usuario.carrera,
                       usuario.correo,
                       usuario.activo,
                       usuario.id
                       ) )
        
        conexion.commit()
        cursor.close()
        conexion.close()

    # DELETE
    def eliminar(self,id):
       conexion = Conexion.obtener_conexion()
       cursor = conexion.cursor()

       cursor.execute("DELETE FROM usuario WHERE id = %s",(id,))

       conexion.commit()
       cursor.close()
       conexion.close()


    def obtener_ultimo_id(self):
       conexion = Conexion.obtener_conexion()
       cursor = conexion.cursor()

       cursor.execute("SELECT MAX(id) FROM usuario")
       resultado = cursor.fetchone()

       cursor.close()
       conexion.close()

       if resultado[0] is None:
           return 0
       return resultado[0] 
    
    def obtener_matricula(self, id):
     conexion = Conexion.obtener_conexion()
     cursor = Conexion.cursor()

     cursor.execute(
        "SELECT matricula FROM usuario WHERE id = %s",
        (id,)
    )

     resultado = cursor.fetchone()

     cursor.close()
     conexion.close()

     if resultado is None:
        return None

     return resultado[0]