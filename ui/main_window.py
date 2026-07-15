import flet as ft

from ui.libro_form import libro_form

def main_window(page: ft.Page):

    # Configurar página
    page.title = "Sistema de Gestión de Biblioteca"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_500

    # Elementos del contenedor principal
    titulo = ft.Text(
        "Sistema de Gestión de Biblioteca",
        size = 24,
        weight = ft.FontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Seleccione una opción del menú",
        size = 16,
        color = ft.Colors.BLUE_GREY_600
    )

    # Creación del contenedor principal
    contenido = ft.Container(
        padding = 30,
        expand = True
    )

    def inicio():
        return ft.Column(
            controls= [
                titulo,
                subtitulo
            ],
            spacing= 10,
        )
    def mostrar_inicio(e=None):
        contenido.content = inicio()
        page.update()
    
    def mostrar_insertar_libro(e= None):
        contenido.content = libro_form(mostrar_inicio)
        page.update()

    # Creación del menú lateral
    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.Colors.BLUE_GREY_900,
        padding = 20,
        content = ft.Column(
            controls =[
                ft.Text(
                    "Biblioteca",
                    size = 22,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de Gestión",
                    size = 12,
                    color = ft.Colors.WHITE
                ),
                ft.Divider(color=ft.Colors.BLUE_GREY_700),
                #botones

                ft.ElevatedButton(
                    "inicio",
                    icon = ft.Icons.HOME,
                    width = 180,
                    on_click = mostrar_inicio
                ),
                ft.ElevatedButton(
                    "Libros",
                    icon = ft.Icons.BOOK,
                    width = 180,
                    on_click= mostrar_insertar_libro
                ),
                ft.ElevatedButton(
                    "Usuarios",
                    icon = ft.Icons.PERSON,
                    width = 180
                ),
                ft.ElevatedButton(
                    "Préstamos",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180
                ), 
                ft.ElevatedButton(
                    "Devoluciones",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180
                ),                                               
            ],
            spacing=15
        )
    )

    # Layout de la página
    layout = ft.Row(
        controls=[
            menu_lateral,
            contenido
        ],
        expand=True
    )
    #Agregar layout a la pagina
    page.add(layout)

    mostrar_inicio() #Mostrar la vista de incio al cargar la pagina