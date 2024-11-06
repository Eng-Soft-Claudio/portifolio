# Bibliotecas
from tkinter import *
from PIL import Image, ImageTk

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

# Desenhar linhas azuis nas direções nordeste, sudeste, sudoeste e noroeste
canvas.create_line(650, 330, 765, 215, fill="blue", width=2)  # Nordeste
canvas.create_line(650, 430, 790, 570, fill="blue", width=2)  # Sudeste
canvas.create_line(550, 430, 410, 570, fill="blue", width=2)  # Sudoeste
canvas.create_line(550, 330, 435, 215, fill="blue", width=2)  # Noroeste

# Adicionar retângulos representando os semáforos
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
        'retangulo': canvas.create_rectangle(725, 120, 800, 255, outline="blue", fill="#add8e6", width=2),
        'luz': [
            canvas.create_oval(750, 135, 775, 160, fill="darkred"),  # Luz vermelha
            canvas.create_oval(750, 170, 775, 195, fill="darkorange"),  # Luz amarela
            canvas.create_oval(750, 205, 775, 230, fill="darkgreen"),  # Luz verde
        ]
    },
    'superior': {
        'retangulo': canvas.create_rectangle(400, 120, 475, 255, outline="blue", fill="#add8e6", width=2),
        'luz': [
            canvas.create_oval(425, 135, 450, 160, fill="darkred"),  # Luz vermelha
            canvas.create_oval(425, 170, 450, 195, fill="darkorange"),  # Luz amarela
            canvas.create_oval(425, 205, 450, 230, fill="darkgreen"),  # Luz verde
        ]
    },
    'esquerda': {
        'retangulo': canvas.create_rectangle(400, 505, 475, 650, outline="blue", fill="#add8e6", width=2),
        'luz': [
            canvas.create_oval(420, 525, 445, 550, fill="darkred"),  # Luz vermelha
            canvas.create_oval(420, 560, 445, 585, fill="darkorange"),  # Luz amarela
            canvas.create_oval(420, 595, 445, 620, fill="darkgreen"),  # Luz verde
        ]
    }
}

# Função para alternar as luzes dos semáforos
def alternar_luzes(canvas, semaforos):
    def iniciar_loop():
        ordem = ['inferior', 'direita', 'superior', 'esquerda']
        
        while True:
            for semaforo_ativo in ordem:
                # Acende a luz vermelha em todos os semáforos
                for semaforo in ordem:
                    canvas.itemconfig(semaforos[semaforo]['luz'][0], fill="#fc2003")  # Luz vermelha
                    canvas.itemconfig(semaforos[semaforo]['luz'][1], fill="darkorange")  # Luz amarela apagada
                    canvas.itemconfig(semaforos[semaforo]['luz'][2], fill="darkgreen")  # Luz verde apagada

                # Luz verde do semáforo ativo
                canvas.itemconfig(semaforos[semaforo_ativo]['luz'][0], fill="darkred")  # Apaga luz vermelha
                canvas.itemconfig(semaforos[semaforo_ativo]['luz'][2], fill="#56fc03")  # Acende luz verde
                canvas.update()
                canvas.after(7000)  # Luz verde por 7 segundos

                # Luz amarela do semáforo ativo
                canvas.itemconfig(semaforos[semaforo_ativo]['luz'][2], fill="darkgreen")  # Apaga luz verde
                canvas.itemconfig(semaforos[semaforo_ativo]['luz'][1], fill="yellow")  # Acende luz amarela
                canvas.update()
                canvas.after(3000)  # Luz amarela por 3 segundos

                # Retorna à luz vermelha
                canvas.itemconfig(semaforos[semaforo_ativo]['luz'][1], fill="darkorange")  # Apaga luz amarela
                canvas.itemconfig(semaforos[semaforo_ativo]['luz'][0], fill="#fc2003")  # Acende luz vermelha
                canvas.update()

    # Chama a função de loop para iniciar a troca de luzes
    canvas.after(0, iniciar_loop)

# Chamar a função para iniciar o loop de semáforos
alternar_luzes(canvas, semaforos)

# Loop principal da janela
janela.mainloop()
