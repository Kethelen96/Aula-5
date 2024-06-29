#3 - Desenvolva em gráfico  barras:

medias_jose = [10,5,8,9,10,5,4]
medias_jose.sort()

meses = ["fev", "mar", "abril", "maio", "junho", "julho", "agosto"]
         
import matplotlib.pyplot as plt
plt.bar(meses, medias_jose)
plt.title("Medias José")
plt.show()
