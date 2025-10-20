# Aula 19/09/2025 Processamento digital de sinais
# Funções para plotar sinais impulso, degrau e rampa
import numpy as np
import matplotlib.pyplot as plt

def impulso(n): 
    valores = []
    # for valor in range(2*n+1):
    for valor in range(-n, n+1):
        if valor == 0:  
            valores.append(1)
        
        else:
            valores.append(0)

    return valores

# Eixo do tempo discreto
n1 = np.arange(-5, 10)

# Função impulso unitário
delta = np.zeros(len(n1))
delta[n1 == 0] = 1 

# print(impulso(1))
# print(impulso(3))

def degrau(n):
    valores = []
    for valor in range(-n, n+1):
        if valor <0:
            valores.append(0)

        else:
            valores.append(1)

    return valores

# outra forma
n = np.arange(-5, 10)

# Função degrau unitário: 0 para n < 0, 1 para n >= 0
u = np.ones(len(n))
u[n < 0] = 0  # zera os valores negativos

# Exibir o degrau
plt.stem(n, u)
plt.title("Função Degrau Unitário u[n]")
plt.xlabel("n")
plt.ylabel("u[n]")
plt.grid(True)
plt.show()

# print(degrau(3))

def rampa(n):
    valores = []
    for valor in range(-n, n+1):
        if valor <0:
            valores.append(0)
        
        else:
            valores.append(valor)

    return valores

# print(rampa(4))

