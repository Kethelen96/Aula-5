import matplotlib.pyplot as plt

frequencia = [1,56,56,15,9,99,10]
frequencia.sort()
frequencia_letra = ["a","b","c","d","e","f","g"]

#plt.plot(frequencia_letra,frequencia)
#plt.bar(frequencia_letra, frequencia)
plt.pie(frequencia)

plt.grid(True)
plt.show()