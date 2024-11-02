import tkinter as tk
import random
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Variáveis de Processo")
        self.geometry("1200x800")
        self.configure(bg="#f0f0f0")

        # Inicializar valores e limites
        self.pressure_value = 25.0
        self.temperature_value = 22.0
        self.humidity_value = 50.0
        self.level_value = 10.0
        self.pressure_limits = (20.0, 30.0)  # Limites de pressão
        self.temperature_limits = (18.0, 28.0)  # Limites de temperatura
        self.humidity_limits = (40.0, 60.0)  # Limites de umidade
        self.level_limits = (5.0, 15.0)  # Limites de nível

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
        width, height = 550, 350
        x0, y0 = 10, 10
        x1, y1 = x0 + width, y0 + height
        canvas.create_arc((x0, y0, x0 + 2 * radius, y0 + 2 * radius), start=90, extent=90, fill="#d0d0d0", outline="#d0d0d0")
        canvas.create_arc((x1 - 2 * radius, y0, x1, y0 + 2 * radius), start=0, extent=90, fill="#d0d0d0", outline="#d0d0d0")
        canvas.create_arc((x0, y1 - 2 * radius, x0 + 2 * radius, y1), start=180, extent=90, fill="#d0d0d0", outline="#d0d0d0")
        canvas.create_arc((x1 - 2 * radius, y1 - 2 * radius, x1, y1), start=270, extent=90, fill="#d0d0d0", outline="#d0d0d0")
        canvas.create_rectangle((x0 + radius, y0, x1 - radius, y1), fill="#d0d0d0", outline="#d0d0d0")
        canvas.create_rectangle((x0, y0 + radius, x1, y1 - radius), fill="#d0d0d0", outline="#d0d0d0")

        # Adiciona o título da caixa
        title_label = tk.Label(canvas, text=self.box_titles[row * 2 + column], bg="#f0f0f0", fg="black", font=('Helvetica', 14))
        title_label.place(x=x0 + 15, y=y0 + 10, anchor='nw')

        # Criação dos displays e alarmes luminosos
        display_label = tk.Label(canvas, bg="#d0d0d0", fg="black", font=('Helvetica', 20))
        display_label.place(relx=0.5, rely=0.5, anchor='center')
        alarm_label = tk.Label(canvas, text="ALERTA!", bg="#d0d0d0", fg="#d0d0d0", font=('Helvetica', 16))
        alarm_label.place(relx=0.5, rely=0.7, anchor='center')

        # Atribuir os elementos de interface a atributos da classe
        if row == 0 and column == 0:
            self.pressure_display = display_label
            self.pressure_alarm = alarm_label
        elif row == 0 and column == 1:
            self.temperature_display = display_label
            self.temperature_alarm = alarm_label
        elif row == 1 and column == 0:
            self.humidity_display = display_label
            self.humidity_alarm = alarm_label
        elif row == 1 and column == 1:
            self.level_display = display_label
            self.level_alarm = alarm_label

        self.grid_rowconfigure(row, weight=1)
        self.grid_columnconfigure(column, weight=1)

    def update_alarm(self, value, limits, display, alarm):
        if value < limits[0] or value > limits[1]:
            alarm.config(fg="red")  # Alerta luminoso em vermelho
        else:
            alarm.config(fg="#d0d0d0")  # Desativa o alarme

        display.config(text=f"{value:.1f}")

    def simulate_pressure(self):
        self.pressure_value += random.uniform(-0.5, 0.5)
        self.update_alarm(self.pressure_value, self.pressure_limits, self.pressure_display, self.pressure_alarm)
        self.after(100, self.simulate_pressure)

    def simulate_temperature(self):
        self.temperature_value += random.uniform(-0.3, 0.3)
        self.update_alarm(self.temperature_value, self.temperature_limits, self.temperature_display, self.temperature_alarm)
        self.after(100, self.simulate_temperature)

    def simulate_humidity(self):
        self.humidity_value += random.uniform(-1.0, 1.0)
        self.update_alarm(self.humidity_value, self.humidity_limits, self.humidity_display, self.humidity_alarm)
        self.after(100, self.simulate_humidity)

    def simulate_level(self):
        self.level_value += random.uniform(-0.2, 0.2)
        self.update_alarm(self.level_value, self.level_limits, self.level_display, self.level_alarm)
        self.after(100, self.simulate_level)

if __name__ == "__main__":
    app = App()
    app.mainloop()
