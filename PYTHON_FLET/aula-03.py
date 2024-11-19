#  Importando as bibliotecas
import flet as ft

def app(page: ft.Page):

    def captura(event: ft.KeyboardEvent):
        page.add(
            ft.Text(f"Tecla pressionada: {event.key}\nAlt pressionado: {event.alt}\nCTRL pressionado: {event.ctrl}\nShift pressionado: {event.shift}")
        )

    page.on_keyboard_event = captura

    page.add(
        ft.Text("Pressione qualquer tecla ou combinação de teclas usando Alt, CTRL ou Shift", text_align="justify")
    )

ft.app(target=app)


