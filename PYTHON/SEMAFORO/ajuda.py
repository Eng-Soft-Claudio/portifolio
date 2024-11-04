# Bibliotecas
from tkinter import *

# Configuração da janela
janela = Tk()
janela.geometry("1200x800")
janela.resizable(False, False)
janela.configure(bg="#afafaf")

# Canvas para desenhar as linhas e elementos
canvas = Canvas(janela, width=1200, height=800, bg="#afafaf", highlightthickness=0)
canvas.place(x=0, y=0)

# Desenhar o fundo preto como se fossem ruas
canvas.create_rectangle(0, 329, 1200, 429, fill="black")  # Rua horizontal
canvas.create_rectangle(550, 0, 650, 800, fill="black")    # Rua vertical

# Desenhar a linha tracejada amarela no centro da rua horizontal
linha_y = 380  # Altura do centro da rua horizontal
canvas.create_line(0, linha_y, 550, linha_y, fill="yellow", dash=(5, 5))  # Linha horizontal tracejada (parte esquerda)
canvas.create_line(650, linha_y, 1200, linha_y, fill="yellow", dash=(5, 5))  # Linha horizontal tracejada (parte direita)

# Desenhar a linha tracejada amarela no centro da rua vertical
linha_x = 600  # Largura do centro da janela
canvas.create_line(linha_x, 0, linha_x, 330, fill="yellow", dash=(5, 5))  # Linha vertical tracejada (parte superior)
canvas.create_line(linha_x, 430, linha_x, 800, fill="yellow", dash=(5, 5))  # Linha vertical tracejada (parte inferior)

# Adicionar linha de retenção do "PARE"
canvas.create_line(600, 463, 651, 463, fill="white", width=6)  # Linha branca na interseção inferior
canvas.create_line(550, 296, 601, 296, fill="white", width=6)  # Linha branca na interseção superior
canvas.create_line(684, 329, 684, 380, fill="white", width=6)  # Linha branca na interseção direita
canvas.create_line(517, 381, 517, 430, fill="white", width=6)  # Linha branca na interseção esquerda

# Adicionar texto "PARE" nas interseções
canvas.create_text(626, 480, text="PARE", fill="white", font=("Helvetica", 12, "bold"), anchor="center")  # Sinalização na via inferior
canvas.create_text(576, 280, text="PARE", fill="white", font=("Helvetica", 12, "bold"), anchor="center", angle=180)  # Sinalização na via superior
canvas.create_text(500, 405, text="PARE", fill="white", font=("Helvetica", 12, "bold"), anchor="center", angle=270)  # Sinalização na via esquerda
canvas.create_text(700, 355, text="PARE", fill="white", font=("Helvetica", 12, "bold"), anchor="center", angle=90)  # Sinalização na via direita

# Criar semáforos nas interseções
semaforos = {
    'inferior': {
        'retangulo': canvas.create_rectangle(725, 505, 800, 650, outline="blue", fill="#add8e6", width=2),
        'luz': [
            canvas.create_oval(750, 525, 775, 550, fill="darkred"),  # Luz vermelha
            canvas.create_oval(750, 560, 775, 585, fill="darkorange"),  # Luz amarela
            canvas.create_oval(750, 595, 775, 620, fill="darkgreen"),  # Luz verde
        ]
    },
    'direita': {
        'retangulo': canvas.create_rectangle(850, 180, 1000, 255, outline="blue", fill="#add8e6", width=2),
        'luz': [
            canvas.create_oval(875, 190, 900, 215, fill="darkred"),  # Luz vermelha
            canvas.create_oval(875, 225, 900, 250, fill="darkorange"),  # Luz amarela
            canvas.create_oval(875, 260, 900, 285, fill="darkgreen"),  # Luz verde
        ]
    },
    'superior': {
        'retangulo': canvas.create_rectangle(400, 50, 475, 195, outline="blue", fill="#add8e6", width=2),
        'luz': [
            canvas.create_oval(425, 70, 450, 95, fill="darkred"),  # Luz vermelha
            canvas.create_oval(425, 105, 450, 130, fill="darkorange"),  # Luz amarela
            canvas.create_oval(425, 140, 450, 165, fill="darkgreen"),  # Luz verde
        ]
    },
    'esquerda': {
        'retangulo': canvas.create_rectangle(200, 300, 275, 450, outline="blue", fill="#add8e6", width=2),
        'luz': [
            canvas.create_oval(225, 320, 250, 345, fill="darkred"),  # Luz vermelha
            canvas.create_oval(225, 355, 250, 380, fill="darkorange"),  # Luz amarela
            canvas.create_oval(225, 390, 250, 415, fill="darkgreen"),  # Luz verde
        ]
    }
}

# Função para alternar as luzes dos semáforos
def alternar_luzes(canvas, semaforos):
    def iniciar_loop():
        ordem = ['inferior', 'direita', 'superior', 'esquerda']
        while True:
            for semaforo in ordem:
                # Acende a luz vermelha
                canvas.itemconfig(semaforos[semaforo]['luz'][0], fill="red")
                canvas.update()
                canvas.after(7000)
                canvas.itemconfig(semaforos[semaforo]['luz'][0], fill="darkred")
                canvas.update()

                # Acende a luz amarela
                canvas.itemconfig(semaforos[semaforo]['luz'][1], fill="yellow")
                canvas.update()
                canvas.after(3000)
                canvas.itemconfig(semaforos[semaforo]['luz'][1], fill="darkorange")
                canvas.update()

                # Acende a luz verde
                canvas.itemconfig(semaforos[semaforo]['luz'][2], fill="green")
                canvas.update()
                canvas.after(7000)
                canvas.itemconfig(semaforos[semaforo]['luz'][2], fill="darkgreen")
                canvas.update()

    # Chama a função de loop para iniciar a troca de luzes
    canvas.after(0, iniciar_loop)

# Iniciar a alternância de luzes
alternar_luzes(canvas, semaforos)

# Iniciar a interface gráfica
janela.mainloop()
