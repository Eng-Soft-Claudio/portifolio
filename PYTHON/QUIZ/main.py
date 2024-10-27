import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz de Python")
        self.root.geometry("600x450")  # Tamanho da janela
        self.root.configure(bg="#F0F4F8")  # Fundo principal

        # Estilo da fonte
        self.custom_font = tkFont.Font(family="Helvetica", size=14)

        # Cabeçalho
        self.header = tk.Label(root, text="Quiz de Python", font=tkFont.Font(family="Helvetica", size=18, weight="bold"), bg="#003366", fg="white")
        self.header.pack(fill=tk.X)

        # Frame para organizar os elementos
        self.frame = tk.Frame(root, bg="#FFFFFF", padx=20, pady=20, bd=2, relief=tk.GROOVE)
        self.frame.pack(padx=10, pady=(10, 0), fill=tk.BOTH, expand=True)

        # Label para a pergunta (com largura aumentada)
        self.question_label = tk.Label(self.frame, text="", font=tkFont.Font(family="Helvetica", size=14), wraplength=500, width=50)
        self.question_label.pack(pady=(0, 10))

        # Variáveis para as opções
        self.selected_option = tk.IntVar()  # Variável para armazenar a opção selecionada

        # Opções de resposta (RadioButtons)
        self.option1 = tk.Radiobutton(self.frame, text="", variable=self.selected_option, value=1, bg="white", font=self.custom_font)
        self.option2 = tk.Radiobutton(self.frame, text="", variable=self.selected_option, value=2, bg="white", font=self.custom_font)
        self.option3 = tk.Radiobutton(self.frame, text="", variable=self.selected_option, value=3, bg="white", font=self.custom_font)
        self.option4 = tk.Radiobutton(self.frame, text="", variable=self.selected_option, value=4, bg="white", font=self.custom_font)

        self.option1.pack(anchor="w")
        self.option2.pack(anchor="w")
        self.option3.pack(anchor="w")
        self.option4.pack(anchor="w")

        # Botão de enviar resposta
        self.submit_button = tk.Button(self.frame, text="Enviar Resposta", command=self.check_answer, bg="#4CAF50", fg="white", font=tkFont.Font(family="Helvetica", size=16), bd=0, height=2, width=20)
        self.submit_button.pack(pady=(10, 10))

        # Label de status (inicialmente oculta)
        self.status_label = tk.Label(self.frame, text="", font=tkFont.Font(family="Helvetica", size=14, weight="bold"), wraplength=350, bg="white")
        self.status_label.pack(pady=(10, 10))

        # Inicialização do quiz
        self.score = 0
        self.total_questions = 0
        self.questions = self.load_questions()  # Carrega todas as perguntas
        self.current_question = None
        self.selected_questions = random.sample(self.questions, 10)  # Seleciona 10 perguntas aleatoriamente
        self.load_question()  # Carrega a primeira pergunta

        # Label de placar (inicialmente oculto)
        self.score_label = tk.Label(self.frame, text="", font=tkFont.Font(family="Helvetica", size=14))
        self.score_label.pack(pady=(10, 0))

        # Botão de reiniciar (com fundo laranja)
        self.restart_button = tk.Button(self.frame, text="Reiniciar Quiz", command=self.restart_quiz, bg="#FFA500", fg="white", font=tkFont.Font(family="Helvetica", size=16), bd=0, height=2, width=20)
        self.restart_button.pack(pady=(10, 0))
        self.restart_button.pack_forget()  # Esconde o botão inicialmente

    def load_questions(self):
        # Lista total de 30 perguntas e respostas
        return [
            ("O que é Python?", "a) Uma linguagem de programação", "b) Um sistema operacional", "c) Um software de edição de imagens", "d) Uma base de dados", 1),
            ("Qual é a extensão padrão dos arquivos Python?", "a) .py", "b) .python", "c) .p", "d) .txt", 1),
            ("Como você inicia um comentário em Python?", "a) //", "b) /*", "c) #", "d) <!--", 3),
            ("Qual comando é usado para imprimir no console em Python?", "a) print()", "b) echo()", "c) output()", "d) display()", 1),
            ("Qual das opções a seguir é uma estrutura de controle de repetição em Python?", "a) if", "b) for", "c) while", "d) todas as anteriores", 4),
            ("Como você define uma função em Python?", "a) function myFunction():", "b) def myFunction():", "c) func myFunction():", "d) define myFunction():", 2),
            ("Qual é o resultado da expressão `2 ** 3` em Python?", "a) 6", "b) 8", "c) 9", "d) 5", 2),
            ("O que faz o método `append()` em uma lista?", "a) Adiciona um elemento ao início da lista", "b) Remove um elemento da lista", "c) Adiciona um elemento ao final da lista", "d) Ordena a lista", 3),
            ("Qual é a função para obter a quantidade de elementos em uma lista?", "a) length()", "b) count()", "c) size()", "d) len()", 4),
            ("Como você importaria um módulo em Python?", "a) import myModule", "b) include myModule", "c) load myModule", "d) require myModule", 1),
            ("Qual é o símbolo usado para divisão em Python?", "a) /", "b) //", "c) : ", "d) %", 1),
            ("Como você cria um loop infinito em Python?", "a) while True:", "b) for (;;)", "c) do {} while (true)", "d) loop", 1),
            ("O que é uma lista em Python?", "a) Um tipo de dado que pode conter múltiplos valores", "b) Um comando", "c) Uma função", "d) Uma variável", 1),
            ("Como você adiciona um item no final de uma lista?", "a) insert()", "b) append()", "c) add()", "d) extend()", 2),
            ("Qual é a diferença entre `==` e `is` em Python?", "a) São a mesma coisa", "b) `==` verifica valor e `is` verifica identidade", "c) `==` verifica identidade e `is` verifica valor", "d) Não há diferença", 2),
            ("O que é um dicionário em Python?", "a) Um tipo de dado que associa chaves a valores", "b) Um comando", "c) Uma função", "d) Um método", 1),
            ("Como você cria um dicionário em Python?", "a) d = {}", "b) d = []", "c) d = dict()", "d) Ambas a e c", 4),
            ("Qual é o comando para sair de um loop em Python?", "a) exit", "b) break", "c) stop", "d) continue", 2),
            ("Qual é o operador para concatenar strings em Python?", "a) +", "b) &", "c) concat()", "d) join()", 1),
            ("O que faz a função `range()`?", "a) Gera uma sequência de números", "b) Gera uma lista", "c) Gera um dicionário", "d) Nenhuma das anteriores", 1),
            ("Como você manipula arquivos em Python?", "a) utilizando o comando open()", "b) utilizando o comando file()", "c) utilizando o comando read()", "d) Não é possível", 1),
            ("Qual é a palavra-chave para tratar exceções em Python?", "a) catch", "b) except", "c) handle", "d) try", 2),
            ("Como você inicia um bloco try-except?", "a) try:", "b) catch:", "c) handle:", "d) begin:", 1),
            ("Qual é o símbolo de módulo em Python?", "a) %", "b) /", "c) *", "d) //", 1),
            ("Qual é o método usado para substituir uma substring em uma string?", "a) replace()", "b) substitute()", "c) swap()", "d) change()", 1),
            ("Qual é a função utilizada para ler um arquivo em Python?", "a) read()", "b) open()", "c) file()", "d) input()", 2),
            ("Qual é o método para transformar uma string em minúsculas?", "a) lower()", "b) tolower()", "c) min()", "d) str_lower()", 1),
            ("O que faz a função `sorted()`?", "a) Ordena uma lista", "b) Inverte uma lista", "c) Cria uma lista", "d) Apaga uma lista", 1),
            ("Qual é a diferença entre uma lista e uma tupla em Python?", "a) Listas são imutáveis, tuplas são mutáveis", "b) Listas são mutáveis, tuplas são imutáveis", "c) Ambas são imutáveis", "d) Ambas são mutáveis", 2),
            ("Como você converte um número inteiro em uma string?", "a) str()", "b) int()", "c) convert()", "d) string()", 1),
            ("O que faz a função `zip()` em Python?", "a) Combina duas ou mais listas", "b) Compacta arquivos", "c) Cria um dicionário", "d) Converte tipos de dados", 1),
            ("Como você inicia um projeto Python?", "a) python -m", "b) python -start", "c) python new", "d) python create", 1),
            ("Qual é o resultado de `5 // 2` em Python?", "a) 2", "b) 2.5", "c) 3", "d) 5", 1),
        ]

    def load_question(self):
        if self.selected_questions:  # Verifica se ainda há perguntas disponíveis
            self.current_question = self.selected_questions.pop()  # Remove uma pergunta da lista de selecionadas
            self.question_label.config(text=self.current_question[0])
            self.option1.config(text=self.current_question[1])
            self.option2.config(text=self.current_question[2])
            self.option3.config(text=self.current_question[3])
            self.option4.config(text=self.current_question[4])

            # Reseta a seleção do Radiobutton
            self.selected_option.set(0)
            self.status_label.config(text="", fg="#000000", bg="white")  # Oculta o status
        else:
            self.question_label.config(text="Quiz finalizado!")
            self.option1.pack_forget()
            self.option2.pack_forget()
            self.option3.pack_forget()
            self.option4.pack_forget()
            self.submit_button.pack_forget()  # Esconde o botão de enviar resposta
            self.score_label.config(text=f"Placar: {self.score} Acertos, {self.total_questions - self.score} Erros")
            self.score_label.pack(pady=(10, 0))  # Exibe o placar
            self.restart_button.pack(pady=(10, 0))  # Exibe o botão de reiniciar

    def check_answer(self):
        if self.selected_option.get() == 0:  # Verifica se uma opção foi selecionada
            messagebox.showwarning("Atenção", "Por favor, escolha uma opção!")
            return
        
        user_answer = self.selected_option.get()
        correct_answer = self.current_question[5]

        if user_answer == correct_answer:
            self.status_label.config(text="✔ Acertou!", fg="green", bg="white")
            self.score += 1
        else:
            self.status_label.config(text=f"✘ Errou! A resposta correta era: {self.current_question[correct_answer]}", fg="red", bg="white")
        
        self.total_questions += 1

        # Carrega uma nova pergunta após 2 segundos
        self.root.after(2000, self.load_question)

    def restart_quiz(self):
        self.score = 0
        self.total_questions = 0
        self.selected_questions = random.sample(self.questions, 10)  # Seleciona novas 10 perguntas aleatórias
        self.restart_button.pack_forget()  # Esconde o botão de reiniciar
        self.score_label.pack_forget()  # Esconde o placar
        self.load_question()  # Carrega a primeira pergunta
        self.option1.pack(anchor="w")  # Reexibe as opções de resposta
        self.option2.pack(anchor="w")
        self.option3.pack(anchor="w")
        self.option4.pack(anchor="w")
        
        # Certifique-se de que o botão de enviar resposta esteja disponível
        self.submit_button.pack(pady=(10, 10))  # Reexibe o botão de enviar resposta
        self.status_label.pack_forget()  # Esconde o status inicialmente
        self.status_label.pack(pady=(10, 10))  # Exibe o status abaixo do botão

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
