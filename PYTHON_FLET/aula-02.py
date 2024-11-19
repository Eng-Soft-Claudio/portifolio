# importando biblioteca
import flet as ft

# Função que instacia a aplicação
def main(page):

    def login(event):
        if not entrada_nome.value:
            entrada_nome.error_text = "Insira o nome antes de prosseguir..."
            page.update()
        if not entrada_senha.value:
            entrada_senha.error_text = "Insira a senha antes de prosseguir..."
            page.update()
        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome}\nSenha: {senha}")
            page.clean()
            page.add(ft.Text(f"Olá {nome}\nBem vindo!!!"))
            pass

    entrada_nome = ft.TextField(label="Digite seu nome...", border_radius=30, hover_color= "#9dbda5", )
    entrada_senha = ft.TextField(label="Digite sua senha...",border_radius=30, hover_color= "#9dbda5")
    page.add(
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton("Clique Aqui...", on_click=login)
    )
    pass

# Habilita a abertura da aplicação
ft.app(target=main)
