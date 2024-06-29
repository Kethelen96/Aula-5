#importar bibliotecas (libs)
#consultar intruções de como usar as bibliotecas: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#estabelecendo os dados
def grafico():
    vendas_em_milhoes = [15,20,30,6,89,15]
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

    #criando gráfico
    fig, ax = plt.subplots()
    ax.pie(vendas_em_milhoes, autopct='%1.1f%%')

    

    #rótulos
    ax.set_title("Gráfico de vendas")
    ax.grid(True)


    #integração do gráfico - 

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title("Vendas")

frame_grafico = tk.Frame (root)
frame_grafico.pack()

btn = tk.Button(root, text="Mostrar gráfico", command=grafico)
btn.pack(padx=10)

root.mainloop()