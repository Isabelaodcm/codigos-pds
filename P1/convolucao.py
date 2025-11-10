# Código para implementar a função de convolução, utilizada na questão 4 item ii da P1
import matplotlib.pyplot as plt
import numpy as np

def convolucao(x, h):
    vetor = []
    m = len(x) + len(h) - 1
    for i in range(m):
        soma = 0
        for k in range(len(x)):
            if 0 <= i-k < len(h):
                soma += x[k]*h[i-k]

        vetor.append(float(soma))
    return vetor

n = np.arange(4)

# Função degrau unitário
u = np.ones(len(n))
u[n < 0] = 0 

x = [9000, 500, 500]
h = u*(1.01)**n

c1 = convolucao(x, h)
n = np.arange(len(c1))   
print("convolucao: ", c1)



    