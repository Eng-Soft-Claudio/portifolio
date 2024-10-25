import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import os

# Função para carregar tarefas da planilha
def load_tasks_from_excel():
    # Obter o diretório do arquivo main.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "tarefas.xlsx")

    # Verifica se o arquivo existe antes de tentar carregá-lo
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            tasks.append((row['Tarefa'], row['Data e Hora']))  # Adiciona cada tarefa à lista

# Função para salvar tarefas em uma planilha
def save_tasks_to_excel():
    # Obter o diretório do arquivo main.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "tarefas.xlsx")
    
    df = pd.DataFrame(tasks, columns=["Tarefa", "Data e Hora"])
    df.to_excel(file_path, index=False)

# Função para adicionar uma tarefa
def add_task():
    task = task_entry.get()
    if task:
        # Capitaliza a primeira letra da tarefa
        task = task.capitalize()
        
        # Obter data e hora atuais
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks.append((task, timestamp))  # Armazenar a tarefa e o timestamp
        update_listbox()
        save_tasks_to_excel()  # Salvar na planilha
        task_entry.delete(0, tk.END)  # Limpa o campo de entrada
    else:
        messagebox.showwarning("Atenção", "Você deve inserir uma tarefa.")

# Função para mostrar detalhes da tarefa
def show_details():
    try:
        selected_index = tasks_listbox.curselection()[0]
        task_name, task_time = tasks[selected_index]

        # Criar nova janela
        details_window = tk.Toplevel(window)
        details_window.title("Detalhes da Tarefa")
        details_window.geometry("350x250")  # Alterada a geometria da janela

        # Mostrar informações da tarefa
        tk.Label(details_window, text=f"Tarefa: {task_name}", font=("Arial", 12)).pack(pady=5)
        tk.Label(details_window, text=f"Data: {task_time.split()[0]}", font=("Arial", 12)).pack(pady=5)
        tk.Label(details_window, text=f"Hora: {task_time.split()[1]}", font=("Arial", 12)).pack(pady=5)

        # Campo para inserir comentários com margem padrão
        tk.Label(details_window, text="Comentários:", font=("Arial", 12)).pack(pady=5)
        comment_entry = tk.Entry(details_window, width=40, font=("Arial", 12))
        comment_entry.pack(pady=5)  # Margem padrão restaurada

        # Botão para fechar a janela
        close_button = tk.Button(details_window, text="Fechar", command=details_window.destroy)
        close_button.pack(pady=10)

    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para ver os detalhes.")

# Função para remover a tarefa selecionada
def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks.pop(selected_task_index)  # Remove a tarefa da lista
        update_listbox()
        save_tasks_to_excel()  # Salvar na planilha
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para remover.")

# Função para limpar todas as tarefas
def clear_tasks():
    tasks.clear()  # Limpa a lista de tarefas
    update_listbox()
    save_tasks_to_excel()  # Salvar na planilha

# Função para atualizar a lista de tarefas
def refresh_tasks():
    global tasks
    tasks.clear()  # Limpa a lista atual
    load_tasks_from_excel()  # Carrega as tarefas da planilha
    update_listbox()  # Atualiza a Listbox

# Criar a janela principal
window = tk.Tk()
window.title("Todo List")

# Configurações da interface
window.geometry("600x400")  # Aumentada a largura da janela em 50%
window.resizable(False, False)

# Frame para a entrada de tarefas
frame = tk.Frame(window)
frame.pack(pady=10)

# Campo de entrada de tarefas
task_entry = tk.Entry(frame, width=30, font=("Arial", 14))
task_entry.pack(side=tk.LEFT, padx=10)

# Botão para adicionar tarefas
add_task_button = tk.Button(frame, text="Adicionar Tarefa", command=add_task, font=("Arial", 14))
add_task_button.pack(side=tk.LEFT)

# Lista de tarefas
tasks_listbox = tk.Listbox(window, width=70, height=10, font=("Arial", 14))
tasks_listbox.pack(pady=10)

# Frame para os botões inferiores
button_frame = tk.Frame(window)
button_frame.pack(pady=5)

# Botão para atualizar tarefas
refresh_button = tk.Button(button_frame, text="Atualizar", command=refresh_tasks, font=("Arial", 14))
refresh_button.pack(side=tk.LEFT, padx=5)

# Botão para remover tarefas
remove_task_button = tk.Button(button_frame, text="Remover Tarefa", command=remove_task, font=("Arial", 14))
remove_task_button.pack(side=tk.LEFT, padx=5)

# Botão para limpar todas as tarefas
clear_tasks_button = tk.Button(button_frame, text="Limpar Todas as Tarefas", command=clear_tasks, font=("Arial", 14))
clear_tasks_button.pack(side=tk.LEFT, padx=5)

# Botão para mostrar detalhes da tarefa
details_button = tk.Button(button_frame, text="Detalhes", command=show_details, font=("Arial", 14))
details_button.pack(side=tk.LEFT, padx=5)

# Atualizar a Listbox com as tarefas
def update_listbox():
    tasks_listbox.delete(0, tk.END)  # Limpa a Listbox
    for task, timestamp in tasks:
        tasks_listbox.insert(tk.END, task)  # Insere apenas o nome da tarefa

# Lista para armazenar tarefas e timestamps
tasks = []

# Carregar tarefas da planilha ao iniciar a aplicação
load_tasks_from_excel()

# Rodar o loop da interface
window.mainloop()
