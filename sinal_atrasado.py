# script de uma função que atrasa um sinal discreto e plota tanto o sinal original quanto o atrasado
# e função de média movel que usa o sinal atrasado

import matplotlib.pyplot as plt
import numpy as np
from sinais_elementares import impulso, degrau, rampa

def atraso(x, nd):
    vetor = []
    for i in range(len(x)):
        if i < nd:
            vetor.append(0)

        else:
            vetor.append(x[i-nd])

    return vetor

# Outra forma
# def atraso(x, nd):
#     if nd < 0:
#         print("nd deve ser positivo")

#     array = np.concatenate((np.zeros(nd), x))
#     return array

def mediaMovel(x):
    vetor = []
    x0 = x
    x1 = atraso(x, 1)
    x2 = atraso(x, 2)
    for i in range(len(x)):
        media = (x0[i] + x1[i] + x2[i])/3
        vetor.append(media)

    return vetor

def mediaMovel2(x, nm):
    vetor = []
    for k in range(len(x)):
        soma = 0
        for i in range(nm):
            valorAtrasado = atraso(x, i)
            soma += valorAtrasado[k]
        media = soma/nm
        vetor.append(media)

    return vetor

# f1 = degrau(5)
# f1 = impulso(5)
# f1 = rampa(5)
f1 = [1, 2, 3, 4, 5, 6, 4, 3, 8]
# n = np.arange(50)
# f1 = np.cos(n*np.pi/8)
a1 = atraso(f1, 2)
m1 = mediaMovel2(f1, 3)
print("Sinal: ", f1)
print("Sinal atrasado: ", a1)

print("Media movel 1: ", mediaMovel(f1))
print("Média movel 2: ", mediaMovel2(f1, 3))

# n = np.arange(len(f1))
n = np.arange(-2, len(f1)-2) # para alinhar o gráfico do sinal atrasado
fig, ax = plt.subplots(3, 1) # uma coluna e duas linhas

ax[0].set_title('Sinal original')
ax[1].set_title("Sinal atrasado")
ax[2].set_title("Sinal original(vermelho) x Média Móvel(verde)")
ax[0].stem(n, f1, linefmt="red") 
ax[1].stem(n, a1, linefmt="blue")  
ax[2].stem(n, f1, linefmt="red") 
ax[2].stem(n, m1, linefmt="green") 

plt.xticks(n) # plot mostra todos os numeros inteiros do intervalo
plt.yticks(n) # plot mostra todos os numeros inteiros do intervalo
plt.show()


# # Sinal contínuo (simulado em pontos)
# t = np.linspace(0, 10, 500)        # eixo do tempo
# x = np.sin(t) + 0.5*np.random.randn(len(t))  # sinal original: seno + ruído

# # Média móvel (janela de largura T = 0.5)
# T = 0.5
# N = int(T / (t[1]-t[0]))   # número de amostras que cabem em T
# janela = np.ones(N)/N      # janela retangular normalizada

# y = mediaMovel2(x, 5)  # saída filtrada


# plt.figure(figsize=(10,5))
# plt.plot(t, x, "r-", label="Sinal original")
# plt.plot(t, y, "b-", linewidth=2, label="Média móvel")
# plt.xlabel("t")
# plt.ylabel("Amplitude")
# plt.title("Média Móvel Contínua (aproximação discreta)")
# plt.legend()
# plt.grid(True)
# plt.show()

# # funcao que calcula a media movel de um sinal continuo
# def mediaMovelCont(x, T, dt):
#     N = int(T/dt)
#     vetor = []
#     for k in range(len(x)):
#         soma = 0
#         for i in range(N):
#             valorAtrasado = atraso(x, i)
#             soma += valorAtrasado[k]
#         media = soma/N
#         vetor.append(media)

#     return vetor

# y2 = mediaMovelCont(x, 0.5, t[1]-t[0])
# plt.figure(figsize=(10,5))
# plt.plot(t, x, "r-", label="Sinal original")
# plt.plot(t, y2, "b-", linewidth=2, label="Média móvel contínua")
# plt.xlabel("t")
# plt.ylabel("Amplitude")
# plt.title("Média Móvel Contínua")
# plt.legend()
# plt.grid(True)
# plt.show()
