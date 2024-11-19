import flet as ft
import csv
import os

# Caminho do arquivo CSV onde os dados das vendas serão armazenados
csv_file_path = "vendas.csv"

# Função para verificar se o arquivo CSV existe, e se não, criar e adicionar o cabeçalho
def verificar_csv():
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Cliente", "Quantidade", "Forma de Pagamento"])

# Função para salvar a venda no arquivo CSV
def salvar_venda(cliente, quantidade, forma_pagamento):
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([cliente, quantidade, forma_pagamento])

# Função para carregar as vendas do arquivo CSV
def carregar_vendas():
    vendas = []
    if os.path.exists(csv_file_path):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Pular o cabeçalho
            for row in reader:
                vendas.append({"cliente": row[0], "quantidade": int(row[1]), "forma_pagamento": row[2]})
    return vendas

# Função para filtrar as vendas por nome ou forma de pagamento
def filtrar_vendas(vendas, nome=None, forma_pagamento=None):
    if nome:
        vendas = [venda for venda in vendas if nome.lower() in venda['cliente'].lower()]
    if forma_pagamento:
        vendas = [venda for venda in vendas if forma_pagamento.lower() in venda['forma_pagamento'].lower()]
    return vendas

# Função para a tela de login
def tela_login(page):
    def on_login_click(e):
        usuario = input_usuario.value
        senha = input_senha.value
        if usuario == "claudio" and senha == "XBOX360skyrim":  # Substitua por autenticação real
            page.clean()
            tela_principal(page)
        else:
            page.add(ft.Text("Usuário ou senha incorretos.", color="red", size=18, weight=ft.FontWeight.BOLD))

    input_usuario = ft.TextField(label="Usuário", autofocus=True, border_color="white", height=50)
    input_senha = ft.TextField(label="Senha", password=True, border_color="white", height=50)
    login_btn = ft.ElevatedButton(
        "Login", 
        on_click=on_login_click,
        bgcolor="green", 
        color="white", 
        icon=ft.icons.LOGIN, 
        width=200, 
        height=50,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
    )

    page.add(ft.Column([input_usuario, input_senha, login_btn], alignment=ft.MainAxisAlignment.CENTER))

# Função para a tela principal
def tela_principal(page):
    def on_registro_vendas_click(e):
        page.clean()
        tela_registro_vendas(page)

    def on_visualizar_vendas_click(e):
        page.clean()
        tela_visualizar_vendas(page)

    def on_logout_click(e):
        page.clean()
        tela_login(page)

    registro_vendas_btn = ft.ElevatedButton(
        "Registrar Vendas", 
        on_click=on_registro_vendas_click,
        bgcolor="blue", 
        color="white", 
        icon=ft.icons.ADD_CIRCLE, 
        width=300, 
        height=60,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
    )
    visualizar_vendas_btn = ft.ElevatedButton(
        "Visualizar Vendas", 
        on_click=on_visualizar_vendas_click,
        bgcolor="blue", 
        color="white", 
        icon=ft.icons.VIEW_LIST, 
        width=300, 
        height=60,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
    )
    logout_btn = ft.ElevatedButton(
        "Deslogar", 
        on_click=on_logout_click,
        bgcolor="red", 
        color="white", 
        icon=ft.icons.LOGOUT, 
        width=300, 
        height=60,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
    )

    page.add(ft.Column([registro_vendas_btn, visualizar_vendas_btn, logout_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=20))

# Função para a tela de registro de vendas
def tela_registro_vendas(page):
    nome_cliente = ft.TextField(label="Nome do Cliente", autofocus=True, height=50)
    quantidade_comprada = ft.TextField(label="Quantidade Comprada", keyboard_type="number", height=50)
    seletor_status = ft.Dropdown(
        label="Forma de Pagamento",
        options=[
            ft.dropdown.Option("Pago"),
            ft.dropdown.Option("Prazo")
        ],
        width=300,
        height=50
    )

    def on_salvar_venda_click(e):
        cliente = nome_cliente.value
        quantidade = int(quantidade_comprada.value) if quantidade_comprada.value.isdigit() else 0
        forma_pagamento = seletor_status.value
        if cliente and quantidade > 0 and forma_pagamento:
            salvar_venda(cliente, quantidade, forma_pagamento)
            page.clean()
            page.add(ft.Text("Venda registrada com sucesso!", color="green", size=20))
            page.add(ft.ElevatedButton("Voltar", on_click=lambda e: voltar_para_principal(page)))
        else:
            page.add(ft.Text("Por favor, preencha todos os campos corretamente.", color="red", size=18))

    salvar_venda_btn = ft.ElevatedButton(
        "Salvar Venda", 
        on_click=on_salvar_venda_click,
        bgcolor="green", 
        color="white", 
        icon=ft.icons.SAVE, 
        width=200, 
        height=50,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
    )

    page.add(ft.Column([nome_cliente, quantidade_comprada, seletor_status, salvar_venda_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=20))
    page.add(ft.ElevatedButton("Voltar", on_click=lambda e: voltar_para_principal(page)))

# Função para voltar à tela principal
def voltar_para_principal(page):
    page.clean()
    tela_principal(page)

# Função para a tela de visualizar vendas
def tela_visualizar_vendas(page):
    filtro_nome = ft.TextField(label="Filtrar por Nome do Cliente", autofocus=True, height=50)
    filtro_pagamento = ft.Dropdown(
        label="Filtrar por Forma de Pagamento",
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Pago"),
            ft.dropdown.Option("Prazo")
        ],
        width=300,
        height=50
    )

    def on_filtrar_click(e):
        nome = filtro_nome.value
        forma_pagamento = filtro_pagamento.value if filtro_pagamento.value != "Todos" else None
        vendas = carregar_vendas()
        vendas_filtradas = filtrar_vendas(vendas, nome, forma_pagamento)

        page.clean()

        if vendas_filtradas:
            table_data = [
                [venda['cliente'], venda['quantidade'], venda['forma_pagamento']] for venda in vendas_filtradas
            ]
            table = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Cliente", size=16)),
                    ft.DataColumn(ft.Text("Quantidade", size=16)),
                    ft.DataColumn(ft.Text("Forma de Pagamento", size=16))
                ],
                rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(col, size=14)) for col in row]) for row in table_data]
            )
            page.add(table)
        else:
            page.add(ft.Text("Nenhuma venda encontrada com os filtros aplicados.", color="red", size=18))

        page.add(ft.ElevatedButton("Voltar", on_click=lambda e: voltar_para_principal(page)))

    filtrar_btn = ft.ElevatedButton(
        "Filtrar", 
        on_click=on_filtrar_click,
        bgcolor="blue", 
        color="white", 
        icon=ft.icons.SEARCH, 
        width=200, 
        height=50,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
    )

    page.add(ft.Column([filtro_nome, filtro_pagamento, filtrar_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=20))
    page.add(ft.ElevatedButton("Voltar", on_click=lambda e: voltar_para_principal(page)))

# Função principal
def main(page: ft.Page):
    page.title = "Sistema de Controle de Vendas"
    verificar_csv()  # Verifica ou cria o arquivo CSV
    page.add(ft.Text("Bem-vindo ao Sistema de Controle de Vendas", size=24, weight=ft.FontWeight.BOLD, color="blue"))
    tela_login(page)

# Iniciar a aplicação
ft.app(target=main)
