import tkinter as tk

def soma():
    n1 = float(input_entry.get())
    n2 = float(input_entry2.get())
    soma = n1 + n2
    label_resulato.config(text=soma)

janela = tk.Tk()
janela.geometry('700x600')
janela.title("Testando Tkinter")

texto = tk.Label(janela, text="Calculadora")
texto.pack()

input_entry = tk.Entry(janela)
input_entry.pack()

input_entry2 = tk.Entry(janela)
input_entry2.pack()

botao = tk.Button(janela, text="Clique aqui", command=soma)
botao.pack()

label_resulato = tk.Label(janela, text="Resultado")
label_resulato.pack()


janela.mainloop()