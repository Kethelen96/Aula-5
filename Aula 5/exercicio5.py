import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import Figure
from tkinter import messagebox

import statistics


def calcular_estatistica(lista):
    media = statistics.mean(lista)
    moda = statistics.mode(lista)
    mediana = statistics.median(lista)
    desvio = statistics.stdev(lista)
    varianca = statistics.variance(lista)
    return media, moda, mediana, desvio, varianca


def mostrar_analise():
    empresa1 = [1000,6000,1200,8000,1400]
    empresa1.sort()
    empresa2 = [5000,4000,3000,2000,7000]
    empresa2.sort()
    empresa3 = [1200,1300,8000,3000,15000]
    empresa3.sort()
    empresa4 = [1400,1750,2000,4500,5900]
    empresa4.sort()
    cargo = ["Estagiário", "Vendedor", "Supervisor", "Gestor", "Diretor"]

    empresa_analisada = empresa_var.get()

    if empresa_analisada == "Empresa 1":
        dado = empresa1
    elif empresa_analisada == "Empresa 2":
        dado = empresa2
    elif empresa_analisada == "Empresa 3":
        dado = empresa3
    elif empresa_analisada == "Empresa 4":
        dado = empresa4
    else: 
        messagebox.showerror("Erro - Esse dado não existe")
        return 
media, moda, mediana, desvio, varianca = calcular_estatistica(dado)



Resultado_text = (f'''
                  Media{media}
                  Moda {moda}
                  Mediana {mediana}
                  Variança {varianca}
                  Desvio Padrão {desvio} 
                  ''')

Resultado_label.config(text=Resultado_text)

fig = Figure(figsize=(6,4), dpi = 100)
ax = fig.add_subplot(111)
ax.set_title("Cargos e Salários")
ax.set_xlabel("Cargos")
ax.set_ylabel("Salários")
ax.plot(cargos, dado)
ax.grig(True)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget()

root = tk.Tk()
root.title("Cargos e Salários")
empresa_var = tk.StringVar(value= "Empresa 1")
empresa_opcoes = ["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"]
menu = ttk.Combobox (root, textvariable = empresa_var, values=empresa_opcoes)
menu.pack()

btn = tk.Button(root, text="Analise", command=mostrar_analise)
btn.pack()


Resultado_label = tk.Label(root, text=" ")
Resultado_label.pack(pady=10)


root.mainloop()





