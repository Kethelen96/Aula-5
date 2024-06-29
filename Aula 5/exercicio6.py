# ***DESAFIO SISTEMAS DE VISUALIZAÇÃO DE DADOS***

# - ***2 estruture no tkinter um sistema de visualização através do clique, MOSTRE:
# METRICAS
# GRAFICO DE BARRAS***

import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def grafico_pib():
    pib=[150,300,500,800,150,300,900]
    pib.sort()
    estados=['SP','RS','BA','PE','ES','MT','MS']

    #criando gráfico
    fig, ax = plt.subplots()
    ax.bar(estados, pib)

    #rótulos
    ax.set_xlabel("Estados")
    ax.set_ylabel("PIB")
    ax.set_title("PIB dos Estados")
    ax.grid(True)


    #integração do gráfico - 
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico_pib)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title("PIB")

frame_grafico_pib = tk.Frame(root)
frame_grafico_pib.pack()

btn = tk.Button(root, text="Mostrar gráfico", command=grafico_pib)
btn.pack(padx=10)

root.mainloop()

plt.show()