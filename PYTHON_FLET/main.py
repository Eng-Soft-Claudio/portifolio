import flet as ft

# Função para a tela de login
def tela_login(page):
    def on_login_click(e):
        usuario = input_usuario.value
        senha = input_senha.value
        
        # Verificação de campos vazios
        if not usuario or not senha:
            page.add(ft.Text("Por favor, preencha todos os campos.", color="red", size=18))
        elif usuario == "admin" and senha == "senha123":  # Exemplo de verificação
            page.clean()
            tela_nova(page)  # Após o login, ir para a nova tela vazia
        else:
            page.add(ft.Text("Usuário ou senha incorretos.", color="red", size=18))

    input_usuario = ft.TextField(label="Usuário", autofocus=True, height=50, border_color="#007BFF")
    input_senha = ft.TextField(label="Senha", password=True, height=50, border_color="#007BFF")
    
    login_btn = ft.ElevatedButton(
        "Login", 
        on_click=on_login_click,
        bgcolor="#007BFF",  # Cor de fundo azul
        color="white",  # Texto branco
        width=250, 
        height=50,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25))  # Botão com bordas arredondadas
    )

    page.add(
        ft.Column(
            [
                input_usuario,
                input_senha,
                login_btn,
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Alinhamento central para os itens
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centralizar horizontalmente
            spacing=20  # Espaçamento entre os elementos
        )
    )

    # Alinhar a coluna verticalmente no centro da tela
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

# Função para a nova tela (após o login)
def tela_nova(page):
    # Tela vazia com um título
    page.add(ft.Text("Nova Tela (ainda vazia)", size=20, weight=ft.FontWeight.BOLD))

# Função principal
def main(page: ft.Page):
    page.title = "Tela de Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centraliza o conteúdo verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centraliza o conteúdo horizontalmente
    tela_login(page)

# Iniciar a aplicação
ft.app(target=main)
