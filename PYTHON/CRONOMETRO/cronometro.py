import tkinter as tk
import time

class Cronometro:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronômetro")

        # Variáveis para controlar o tempo
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

        # Criar display
        self.display = tk.Label(master, text=self, font=("Arial", 48))
        self.display.pack(pady=20)

        # Criar botões
        self.start_button = tk.Button(master, text="Iniciar", command=self.start, font=("Arial", 14))
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(master, text="Pausar", command=self.pause, font=("Arial", 14))
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(master, text="Reiniciar", command=self.reset, font=("Arial", 14))
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.update_display()

    def __repr__(self):
        # Formatar o tempo com milissegundos em três dígitos
        minutos = int(self.elapsed_time // 60)
        segundos = int(self.elapsed_time % 60)
        milissegundos = int((self.elapsed_time - int(self.elapsed_time)) * 100)
        return f"{minutos:02d}:{segundos:02d}.{milissegundos:02d}"

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time  # Ajusta o tempo de início
            self.running = True
            self.run_timer()

    def run_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time  # Atualiza o tempo decorrido
            self.update_display()
            self.master.after(10, self.run_timer)  # Atualiza a cada 10 milissegundos

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0  # Resetar o tempo
        self.update_display()

    def update_display(self):
        self.display.config(text=self)

# Criar a janela principal
root = tk.Tk()
cronometro = Cronometro(root)

# Rodar o loop da interface
root.mainloop()
