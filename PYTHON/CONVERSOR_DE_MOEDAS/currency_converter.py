import requests
import tkinter as tk
from tkinter import messagebox, ttk
import locale

# Configuração do locale para formatação em português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Função para obter a taxa de câmbio
def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates'].get(target_currency)
    else:
        return None

# Função para realizar a conversão
def convert_currency():
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()
    amount = amount_entry.get()
    
    if not amount.isdigit() or float(amount) <= 0:
        messagebox.showerror("Erro", "Digite um valor numérico positivo.")
        return
    
    rate = get_exchange_rate(api_key, base_currency, target_currency)
    if rate:
        converted_amount = float(amount) * rate
        # Formatação para moeda brasileira
        result_text = f"{target_currency} $ {locale.format_string('%.2f', converted_amount, grouping=True)}"
        result_label.config(text=result_text)  # Atualiza o texto do Label de resultado
        status_label.config(text="Conversão realizada com sucesso.")
    else:
        messagebox.showerror("Erro", "Falha ao obter a taxa de câmbio.")

# Chave da API
api_key = "e342bd3443af914c94470e92"

# Configuração da janela principal
root = tk.Tk()
root.title("Conversor de Moedas")
root.geometry("300x300")
root.configure(bg='#f8f9fa')

# Frame principal
frame = tk.Frame(root, bg='#f8f9fa')
frame.pack(pady=20)

# Lista de moedas disponíveis
moedas = ['USD', 'EUR', 'GBP', 'JPY', 'BRL', 'CAD', 'AUD', 'CNY', 'INR']

# Elementos da interface
tk.Label(frame, text="Moeda de origem:", bg='#f8f9fa').grid(row=0, column=0, padx=5, pady=5, sticky='e')
base_currency_var = tk.StringVar(root)
base_currency_var.set(moedas[0])
base_currency_menu = ttk.Combobox(frame, textvariable=base_currency_var, values=moedas, state='readonly')
base_currency_menu.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Moeda de destino:", bg='#f8f9fa').grid(row=1, column=0, padx=5, pady=5, sticky='e')
target_currency_var = tk.StringVar(root)
target_currency_var.set(moedas[1])
target_currency_menu = ttk.Combobox(frame, textvariable=target_currency_var, values=moedas, state='readonly')
target_currency_menu.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Valor:", bg='#f8f9fa').grid(row=2, column=0, padx=5, pady=5, sticky='e')
amount_entry = tk.Entry(frame)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

convert_button = tk.Button(frame, text="Converter", command=convert_currency, bg='#4CAF50', fg='white', font=("Helvetica", 12))
convert_button.grid(row=3, columnspan=2, padx=5, pady=10)

# Label para mostrar o resultado da conversão
result_label = tk.Label(frame, text="", font=("Helvetica", 14), bg='#f8f9fa')
result_label.grid(row=4, columnspan=2, padx=5, pady=10)

# Barra de Status
status_label = tk.Label(root, text="", bg='#f8f9fa', fg='blue')
status_label.pack(side=tk.BOTTOM, fill=tk.X)

# Mensagem de crédito na parte inferior
credit_label = tk.Label(root, text="Developed with Python, by Claudio De Lima Tosta", bg='#f8f9fa', font=("Helvetica", 8))
credit_label.pack(side=tk.BOTTOM, pady=5)

# Executar o aplicativo
root.mainloop()
