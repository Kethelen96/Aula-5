#2 - Crie um gráfico plot(linhas) para mostra:

import matplotlib.pyplot as plt

ano = [2021,2022,2023,2024,2025,2026]

vendas = [10000,2000,30000,10000,5000,20000]
vendas.sort()

plt.plot(ano, vendas)
plt.title("Volume de vendas ao ano")
plt.grid(True)
plt.show()