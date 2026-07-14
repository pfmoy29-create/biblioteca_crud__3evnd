import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import flet as ft

from ui.main_window import main_window
from dao.libro_dao import LibroDAO
from Models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from Models.usuarios import Usuario

def ver_todo(libro_dao):
    try:
        
        libros = libro_dao.obtener_libros()

        print("Libros en la biblioteca")
        if len(libros) == 0:
            print("No hay libros en la biblioteca")
        else :
            for libro in libros:
                print(f"{libro.titulo} - {libro.autor} - {libro.disponible}")

        print("\n Conexion exitosa a la base de datos")

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

def insertar_libro(libro_dao):
    try:
        print("------------------------------------")
        print("Inserción de un nuevo libro")
        titulo = input("Escribe el título del libro: ")
        autor = int(input("Escribe el id del autor: "))
        isbn = input("Escribe el ISBN del libro: ")
        disponible = True
        nuevoLibro = Libro(None, titulo, autor, isbn, disponible)
        libro_dao.insertar(nuevoLibro)
    except Exception as e:
        print(f"Error al insertar libro: {e}")
1
def actualizar_libro(libro_dao):
    ver_todo(libro_dao)
    id = int(input("Escribe el id del libro a editar: "))
    print("Actualiza los datos de este libro")
    titulo = input("Escribe el nuevo titulo del libro: ")
    autor = input("Escribe el nuevo id del autor: ")
    isbn = input("Escribe el nuevo isbn del libro: ")
    disponible = input("Escribe si el libro esta disponible o no (si/no): ").strip().lower() == "si"
    libro = Libro(id, titulo, autor, isbn, disponible)
    libro_dao.actualizar(libro)

def eliminar_libro(libro_dao):
    ver_todo(libro_dao)
    id = int(input("Escribe el id del libro a eliminar: "))
    libro_dao.eliminar(id)
    print("Libros Disponibles")
    ver_todo(libro_dao)

def menu_libros():
    libro_dao = LibroDAO()

    # Imprime el menú de opciones
    print("1. Ver todos los libros")
    print("2. Insertar nuevo libro")
    print("3. Actualizar un libro existente")
    print("4. Eliminar un libro existente")

    opcion = int(input("Escribe una opcion (1-4): "))

    match opcion:
        case 1:ver_todo(libro_dao)
        case 2:insertar_libro(libro_dao)
        case 3:actualizar_libro(libro_dao)
        case 4:eliminar_libro(libro_dao)


def ver_usuarios(usuario_dao):
    try:
        usuarios = usuario_dao.obtener_usuarios()
        print("Usuarios en la biblioteca")
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            for usuario in usuarios:
                print(f"{usuario.id} - {usuario.nombre} - {usuario.matricula} - {usuario.carrera} - {usuario.correo} - {usuario.activo}")
        print("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

def insertar_usuario(usuario_dao):
    try:
        print("------------------------------------")
        print("Inserción de un nuevo usuario")
        nombre = input("Escribe el nombre del usuario: ")
        matricula = input("Escribe la matrícula del usuario: ")
        carrera = int(input("Escribe el id de la carrera: "))
        correo = input("Escribe el correo del usuario: ")
        activo = True
        nuevoUsuario = Usuario(None, nombre, matricula, carrera, correo, activo)
        usuario_dao.insertar(nuevoUsuario)
    except Exception as e:
        print(f"Error al insertar usuario: {e}")

def actualizar_usuario(usuario_dao):
    ver_usuarios(usuario_dao)
    id = int(input("Escribe el id del usuario a editar: "))
    print("Actualiza los datos de este usuario")
    nombre = input("Escribe el nuevo nombre del usuario: ")
    matricula = input("Escribe la nueva matrícula: ")
    carrera = int(input("Escribe el nuevo id de la carrera: "))
    correo = input("Escribe el nuevo correo: ")
    activo = input("Escribe si el usuario esta activo o no (si/no): ").strip().lower() == "si"
    usuario = Usuario(id, nombre, matricula, carrera, correo, activo)
    usuario_dao.actualizar(usuario)

def eliminar_usuario(usuario_dao):
    ver_usuarios(usuario_dao)
    id = int(input("Escribe el id del usuario a eliminar: "))
    usuario_dao.eliminar(id)
    print("Usuarios Disponibles")
    ver_usuarios(usuario_dao)

def menu_usuarios():
    usuario_dao = UsuarioDAO()

    # Imprime el menú de opciones
    print("1. Ver todos los usuarios")
    print("2. Insertar nuevo usuario")
    print("3. Actualizar un usuario existente")
    print("4. Eliminar un usuario existente")

    opcion = int(input("Escribe una opcion (1-4): "))

    match opcion:
        case 1:ver_usuarios(usuario_dao)
        case 2:insertar_usuario(usuario_dao)
        case 3:actualizar_usuario(usuario_dao)
        case 4:eliminar_usuario(usuario_dao)

ft.app(target = main_window)
# def main():
#     print("=== Biblioteca Universitaria ==")
#     print("=== Menú de opciones ==")
#     print("1. Gestión de libros")
#     print("2. Gestión de usuarios")

#     opcion = int(input("Escribe tu opcion: "))

#     match opcion:
#         case 1: menu_libros()
#         case 2: menu_usuarios()

# if _name_ == "_main_":
#     main()