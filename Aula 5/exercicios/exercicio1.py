#Exercicio 1 - Identifique o eixo x e y e adapte esse código para mostrar o gráfico

import statistics


def moda1(lista):
    moda = statistics.mode(lista)
    print('Moda: ', moda)


def mediana1(lista):
    mediana = statistics.median(lista)
    print('Mediana: ', mediana)


def varianca1(lista):
    varianca = statistics.variance(lista)
    print('Variança: ', varianca)

def desvio1(lista):
    desvio = statistics.stdev(lista)
    print(f'Desvio padrão:  {desvio:.2f}')


def media1(lista):
    media = statistics.mean(lista)
    print('Media: ', media)
 



empresa1 = [1000,6000,1200,8000]
empresa1.sort()
empresa2 = [5000,4000,3000,2000]
empresa2.sort()
empresa3 = [1200,1300,8000,3000]
empresa3.sort()
empresa4 = [1400,1750,2000,4500]
empresa4.sort()

def handle(lista, salarios):

    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)


handle(empresa1, empresa1)  
handle(empresa2, empresa2)   
handle(empresa3, empresa3) 
handle(empresa4, empresa4)

enter=input('enter para sair')

import matplotlib.pyplot as plt

empresas = (empresa1, empresa2, empresa3, empresa4)
cargos = ("Analista", "Supervisor", "Cordenador", "Gerente")

plt.plot(cargos, empresas)
plt.grid(True)
plt.title("Salários e Cargos")
plt.show()
