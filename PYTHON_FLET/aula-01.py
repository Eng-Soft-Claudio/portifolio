# Importando biblioteca
import flet as ft

# Função que instacia a aplicação
def main(page: ft.Page):
    texto = ft.Text(value="Olá, Mundo!!", size=100)
    page.controls.append(texto)
    page.update()

# Comando que habilita a aplicação
ft.app(target=main)