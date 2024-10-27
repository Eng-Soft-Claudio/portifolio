import tkinter as tk
from math import sqrt

# Variáveis globais para armazenar o valor anterior e o operador
previous_value = ""
operator = ""

# Função para atualizar o display
def update_display(value):
    current_text = display_var.get()
    display_var.set(current_text + value)

# Função para limpar o display
def clear_display():
    display_var.set("")
    global previous_value, operator
    previous_value = ""
    operator = ""

# Função para armazenar o operador e limpar o display
def handle_operator(op):
    global previous_value, operator
    previous_value = display_var.get().replace(',', '.')  # Converter "," para "." ao armazenar
    operator = op
    display_var.set("")

# Função para calcular o resultado
def calculate():
    try:
        current_value = display_var.get().replace(',', '.')  # Converter "," para "."
        if operator:
            expression = previous_value + operator + current_value
            result = eval(expression)
            display_var.set(str(result).replace('.', ','))  # Converter "." para "," na exibição
    except Exception as e:
        display_var.set("Erro")

# Função para calcular a raiz quadrada
def calculate_sqrt():
    try:
        result = sqrt(float(display_var.get().replace(',', '.')))  # Converter "," para "."
        display_var.set(str(result).replace('.', ','))  # Converter "." para "," na exibição
    except Exception as e:
        display_var.set("Erro")

# Função para calcular porcentagem
def calculate_percentage():
    try:
        result = float(display_var.get().replace(',', '.')) / 100  # Converter "," para "."
        display_var.set(str(result).replace('.', ','))  # Converter "." para "," na exibição
    except Exception as e:
        display_var.set("Erro")

# Criar a janela principal
window = tk.Tk()
window.title("Calculadora")

# Impedir o redimensionamento da janela
window.resizable(False, False)

# Variável para o display
display_var = tk.StringVar()

# Display aumentado em 1/2 no tamanho e na fonte, alinhado à direita, com margem externa
display = tk.Entry(window, textvariable=display_var, font=("Arial", 30), bd=10, insertwidth=6, width=21, borderwidth=4, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Margem externa adicionada aqui

# Tamanho dos botões reduzido para 3/4 do tamanho original, largura diminuída
button_size = {'padx': 10, 'pady': 10, 'font': ("Arial", 13), 'width': 5}  # Largura reduzida

# Linha superior: C, raiz quadrada, %, /
tk.Button(window, text="C", **button_size, command=clear_display).grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
tk.Button(window, text="√", **button_size, command=calculate_sqrt).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
tk.Button(window, text="%", **button_size, command=calculate_percentage).grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
tk.Button(window, text="/", **button_size, command=lambda: handle_operator('/')).grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

# Botões numéricos
buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3'
]

row = 2
col = 0

for button in buttons:
    tk.Button(window, text=button, **button_size, command=lambda b=button: update_display(b)).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    
    col += 1
    if col > 2:
        col = 0
        row += 1

# Linha inferior: 0, ., =
tk.Button(window, text="0", **button_size, command=lambda: update_display('0')).grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
tk.Button(window, text=",", **button_size, command=lambda: update_display(',')).grid(row=5, column=2, sticky="nsew", padx=5, pady=5)  # Alterado para ","
tk.Button(window, text="=", **button_size, command=calculate).grid(row=5, column=3, sticky="nsew", padx=5, pady=5)

# Botões de operadores: +, -, *
tk.Button(window, text="*", **button_size, command=lambda: handle_operator('*')).grid(row=2, column=3, sticky="nsew", padx=5, pady=5)
tk.Button(window, text="-", **button_size, command=lambda: handle_operator('-')).grid(row=3, column=3, sticky="nsew", padx=5, pady=5)
tk.Button(window, text="+", **button_size, command=lambda: handle_operator('+')).grid(row=4, column=3, sticky="nsew", padx=5, pady=5)

# Adicionar a frase abaixo da calculadora
label = tk.Label(window, text="Developed with Python, by Claudio De Lima Tosta", font=("Arial", 8))
label.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

# Rodar o loop da interface
window.mainloop()
