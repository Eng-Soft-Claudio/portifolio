import tkinter as tk
import random
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Variáveis de Processo")
        self.geometry("1200x800")  # Tamanho da janela principal
        self.configure(bg="#f0f0f0")  # Cor de fundo da janela

        # Inicializar os valores
        self.pressure_value = 25.0  # Valor inicial da pressão
        self.temperature_value = 22.0  # Valor inicial da temperatura
        self.humidity_value = 50.0  # Valor inicial da umidade
        self.level_value = 10.0  # Valor inicial do nível
        self.direction = 1  # Direção para pressão
        self.change_direction_time = time.time()  # Tempo da última mudança

        # Nomes distintos para cada caixa
        self.box_titles = ["PRESSÃO (kg/cm²)", "TEMPERATURA (°C)", "UMIDADE (%)", "NÍVEL (mmH²O)"]

        # Criar 4 caixas em um grid 2x2
        for i in range(2):
            for j in range(2):
                self.create_box(i, j)

        # Iniciar simulações
        self.simulate_pressure()
        self.simulate_temperature()
        self.simulate_humidity()
        self.simulate_level()

    def create_box(self, row, column):
        # Canvas para desenhar bordas arredondadas
        canvas = tk.Canvas(self, bg="#f0f0f0", highlightthickness=0)
        canvas.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        # Desenhar um retângulo arredondado
        radius = 20
        width, height = 550, 350  # Dimensões da caixa
        x0, y0 = 10, 10
        x1, y1 = x0 + width, y0 + height
        canvas.create_arc((x0, y0, x0 + 2 * radius, y0 + 2 * radius), start=90, extent=90, fill="#d0d0d0", outline="#d0d0d0")
        canvas.create_arc((x1 - 2 * radius, y0, x1, y0 + 2 * radius), start=0, extent=90, fill="#d0d0d0", outline="#d0d0d0")
        canvas.create_arc((x0, y1 - 2 * radius, x0 + 2 * radius, y1), start=180, extent=90, fill="#d0d0d0", outline="#d0d0d0")
        canvas.create_arc((x1 - 2 * radius, y1 - 2 * radius, x1, y1), start=270, extent=90, fill="#d0d0d0", outline="#d0d0d0")
        canvas.create_rectangle((x0 + radius, y0, x1 - radius, y1), fill="#d0d0d0", outline="#d0d0d0")
        canvas.create_rectangle((x0, y0 + radius, x1, y1 - radius), fill="#d0d0d0", outline="#d0d0d0")

        # Altera o título da caixa com base no índice da caixa
        title_label = tk.Label(canvas, text=self.box_titles[row * 2 + column], bg="#f0f0f0", fg="black", font=('Helvetica', 14))
        title_label.place(x=x0 + 15, y=y0 + 10, anchor='nw')  # Posição do título

        # Adiciona labels com base na caixa
        if row == 0 and column == 0:  # Pressão
            self.pressure_display = tk.Label(canvas, text=f"{self.pressure_value:.1f} kg/cm²", bg="#d0d0d0", fg="black", font=('Helvetica', 20))
            self.pressure_display.place(relx=0.5, rely=0.5, anchor='center')  # Centraliza na caixa
            self.alarm_label = tk.Label(canvas, text="", bg="#d0d0d0", fg="red", font=('Helvetica', 16))
            self.alarm_label.place(relx=0.5, rely=0.7, anchor='center')
            self.alarm_label.config(fg="#d0d0d0")  # Inicialmente oculto

        elif row == 0 and column == 1:  # Temperatura
            self.temperature_display = tk.Label(canvas, text=f"{self.temperature_value:.1f} °C", bg="#d0d0d0", fg="black", font=('Helvetica', 20))
            self.temperature_display.place(relx=0.5, rely=0.5, anchor='center')

        elif row == 1 and column == 0:  # Umidade
            self.humidity_display = tk.Label(canvas, text=f"{self.humidity_value:.1f} %", bg="#d0d0d0", fg="black", font=('Helvetica', 20))
            self.humidity_display.place(relx=0.5, rely=0.5, anchor='center')

        elif row == 1 and column == 1:  # Nível
            self.level_display = tk.Label(canvas, text=f"{self.level_value:.1f} mmH²O", bg="#d0d0d0", fg="black", font=('Helvetica', 20))
            self.level_display.place(relx=0.5, rely=0.5, anchor='center')

        # Configura o grid para redimensionar as caixas corretamente
        self.grid_rowconfigure(row, weight=1)
        self.grid_columnconfigure(column, weight=1)

    def simulate_pressure(self):
        current_time = time.time()  # Tempo atual em segundos
        if current_time - self.change_direction_time >= 5:  # 5 segundos
            self.direction = random.choice([-1, 1])  # -1 para diminuir, 1 para aumentar
            self.change_direction_time = current_time  # Atualiza o tempo da última mudança

        # Atualiza pressão
        self.pressure_value += self.direction * 0.2
        self.pressure_value = max(20.0, min(30.0, self.pressure_value))  # Limites

        # Atualiza display e alarme
        self.pressure_display.config(text=f"{self.pressure_value:.1f} kg/cm²")
        if self.pressure_value <= 22:
            self.alarm_label.config(text="Pressão Baixa!")
        elif self.pressure_value >= 28:
            self.alarm_label.config(text="Pressão Alta!")
        else:
            self.alarm_label.config(text="")

        # Chama a função novamente após 200ms
        self.after(200, self.simulate_pressure)

    def simulate_temperature(self):
        # Simulação de temperatura
        self.temperature_value += random.uniform(-0.5, 0.5)  # Variação aleatória
        self.temperature_value = max(15.0, min(30.0, self.temperature_value))  # Limites
        self.temperature_display.config(text=f"{self.temperature_value:.1f} °C")
        self.after(2000, self.simulate_temperature)  # Atualiza a cada 2 segundos

    def simulate_humidity(self):
        # Simulação de umidade
        self.humidity_value += random.uniform(-1.0, 1.0)  # Variação aleatória
        self.humidity_value = max(0.0, min(100.0, self.humidity_value))  # Limites
        self.humidity_display.config(text=f"{self.humidity_value:.1f} %")
        self.after(3000, self.simulate_humidity)  # Atualiza a cada 3 segundos

    def simulate_level(self):
        # Simulação de nível
        self.level_value += random.uniform(-0.2, 0.2)  # Variação aleatória
        self.level_value = max(0.0, min(50.0, self.level_value))  # Limites
        self.level_display.config(text=f"{self.level_value:.1f} mmH²O")
        self.after(4000, self.simulate_level)  # Atualiza a cada 4 segundos

if __name__ == "__main__":
    app = App()
    app.mainloop()
