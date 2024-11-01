import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel

# Caminho do arquivo CSV
csv_file_path = "PYTHON/CONTROLE_VENDAS/vendas.csv"

# Função para carregar os dados do CSV
def load_data():
    try:
        return pd.read_csv(csv_file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Nome do Comprador", "Valor Total", "Quantidade", "Forma de Pagamento", "Status do Pagamento"])

# Função para salvar os dados no CSV
def save_data(df):
    df.to_csv(csv_file_path, index=False)

# Função para atualizar a Treeview com os dados do CSV
def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    df = load_data()
    for _, row in df.iterrows():
        formatted_row = list(row)
        formatted_row[1] = f"R$ {formatted_row[1]:,.2f}".replace('.', ',')  # Formatação do valor total
        tree.insert("", "end", values=formatted_row)
    update_sums()  # Atualiza as somas após carregar os dados

# Função para abrir a janela de adição de vendas
def open_add_sale_window():
    add_sale_window = Toplevel(root)
    add_sale_window.title("Adicionar Nova Venda")
    add_sale_window.geometry("400x300")
    add_sale_window.config(bg="#EAEFF1")  # Cor de fundo azul suave

    tk.Label(add_sale_window, text="Nome do Comprador:", bg="#EAEFF1").pack(pady=5)
    entry_name = tk.Entry(add_sale_window)
    entry_name.pack(pady=5)

    tk.Label(add_sale_window, text="Quantidade:", bg="#EAEFF1").pack(pady=5)
    entry_quantity = tk.Entry(add_sale_window)
    entry_quantity.pack(pady=5)

    tk.Label(add_sale_window, text="Forma de Pagamento:", bg="#EAEFF1").pack(pady=5)
    entry_payment_method = ttk.Combobox(add_sale_window, values=["Prazo", "Dinheiro", "Pix"])
    entry_payment_method.pack(pady=5)

    def add_sale():
        name = entry_name.get()
        quantity = entry_quantity.get()
        payment_method = entry_payment_method.get()

        if not name or not quantity or payment_method == "":
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")
            return

        total_value = quantity * 7.00  # Valor total fixo
        status_payment = "PAGO" if payment_method in ["Dinheiro", "Pix"] else "EM ABERTO"

        new_data = [name, total_value, quantity, payment_method, status_payment]
        df = load_data()
        df.loc[len(df)] = new_data
        save_data(df)
        update_treeview()
        add_sale_window.destroy()

    tk.Button(add_sale_window, text="Adicionar Venda", command=add_sale, bg="lightblue").pack(pady=10)

# Função para excluir uma venda selecionada
def delete_sale():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Seleção Necessária", "Selecione uma linha para excluir.")
        return

    selected_id = tree.index(selected[0])  # Obtém o índice selecionado
    if messagebox.askyesno("Confirmação", "Deseja realmente excluir esta venda?"):
        df = load_data()
        df = df.drop(selected_id).reset_index(drop=True)  # Remove a linha selecionada
        save_data(df)  # Salva as alterações no CSV
        update_treeview()  # Atualiza a Treeview

# Função para marcar como pago uma venda a prazo
def mark_as_paid():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Seleção Necessária", "Selecione uma linha para marcar como pago.")
        return

    selected_id = tree.index(selected[0])  # Obtém o índice selecionado
    df = load_data()

    if df.at[selected_id, "Forma de Pagamento"] != "Prazo":
        messagebox.showwarning("Atenção", "A opção 'Marcar como Pago' é válida apenas para vendas a prazo.")
        return

    df.at[selected_id, "Status do Pagamento"] = "PAGO"
    save_data(df)
    update_treeview()

# Função para atualizar as somas
def update_sums():
    df = load_data()
    
    # Filtra as vendas
    total_avista_dinheiro = df[df["Forma de Pagamento"] == "Dinheiro"]["Valor Total"].sum()
    total_avista_pix = df[df["Forma de Pagamento"] == "Pix"]["Valor Total"].sum()
    
    # Totaliza as vendas a prazo com base no status de pagamento
    total_aprazo_pago = df[(df["Forma de Pagamento"] == "Prazo") & (df["Status do Pagamento"] == "PAGO")]["Valor Total"].sum()
    total_aprazo_deve = df[(df["Forma de Pagamento"] == "Prazo") & (df["Status do Pagamento"] == "EM ABERTO")]["Valor Total"].sum()

    # Atualiza os rótulos com as somas
    label_total_avista_dinheiro.config(text=f"Total Vendas à Vista (Dinheiro): R$ {total_avista_dinheiro:,.2f}".replace('.', ','))
    label_total_avista_pix.config(text=f"Total Vendas à Vista (Pix): R$ {total_avista_pix:,.2f}".replace('.', ','))
    label_total_aprazo_pago.config(text=f"Total Vendas a Prazo (Pagas): R$ {total_aprazo_pago:,.2f}".replace('.', ','))
    label_total_aprazo_deve.config(text=f"Total Vendas a Prazo (Em Aberto): R$ {total_aprazo_deve:,.2f}".replace('.', ','))

# Configuração da interface gráfica
root = tk.Tk()
root.title("Controle de Vendas")
root.geometry("1000x500")
root.config(bg="#EAEFF1")  # Cor de fundo azul suave

# Criação do Frame com margem externa para a Treeview
tree_frame = tk.Frame(root, bg="#EAEFF1", padx=10, pady=10)  # Margem de 10 pixels
tree_frame.pack(fill="both", expand=True)

# Treeview para exibir vendas dentro do frame com margem
tree = ttk.Treeview(tree_frame, columns=("Nome do Comprador", "Valor Total", "Quantidade", "Forma de Pagamento", "Status do Pagamento"), show="headings")
tree.heading("Nome do Comprador", text="Nome do Comprador")
tree.heading("Valor Total", text="Valor Total")
tree.heading("Quantidade", text="Quantidade")
tree.heading("Forma de Pagamento", text="Forma de Pagamento")
tree.heading("Status do Pagamento", text="Status do Pagamento")

# Alinhamento das colunas
tree.column("Nome do Comprador", anchor="e")  # Alinhado à direita
tree.column("Valor Total", anchor="e")  # Alinhado à direita
tree.column("Quantidade", anchor="center")  # Centralizado
tree.column("Forma de Pagamento", anchor="e")  # Alinhado à direita
tree.column("Status do Pagamento", anchor="e")  # Alinhado à direita

tree.pack(fill="both", expand=True)

# Frame para os totais de vendas e botões
bottom_frame = tk.Frame(root, bg="#D9E6F2")  # Fundo mais claro
bottom_frame.pack(fill="x", side="bottom")

# Frame para informações de totais de vendas
totals_frame = tk.Frame(bottom_frame, bg="#D9E6F2", padx=10, pady=10)
totals_frame.pack(side="left", fill="both", expand=True)

label_total_avista_dinheiro = tk.Label(totals_frame, text="Total Vendas à Vista (Dinheiro): R$ 0,00", bg="#D9E6F2")
label_total_avista_pix = tk.Label(totals_frame, text="Total Vendas à Vista (Pix): R$ 0,00", bg="#D9E6F2")
label_total_aprazo_pago = tk.Label(totals_frame, text="Total Vendas a Prazo (Pagas): R$ 0,00", bg="#D9E6F2")
label_total_aprazo_deve = tk.Label(totals_frame, text="Total Vendas a Prazo (Em Aberto): R$ 0,00", bg="#D9E6F2")

label_total_avista_dinheiro.pack(anchor="w")
label_total_avista_pix.pack(anchor="w")
label_total_aprazo_pago.pack(anchor="w")
label_total_aprazo_deve.pack(anchor="w")

# Frame para os botões
button_frame = tk.Frame(bottom_frame, bg="#D9E6F2", padx=10, pady=10)
button_frame.pack(side="right", fill="both")

tk.Button(button_frame, text="Adicionar Venda", command=open_add_sale_window, bg="lightblue").pack(fill="x", pady=2)
tk.Button(button_frame, text="Excluir Venda", command=delete_sale, bg="lightcoral").pack(fill="x", pady=2)
tk.Button(button_frame, text="Marcar como Pago", command=mark_as_paid, bg="lightyellow").pack(fill="x", pady=2)

# Atualiza a Treeview com os dados do CSV ao iniciar
update_treeview()

root.mainloop()
