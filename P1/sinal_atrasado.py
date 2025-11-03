# script de uma função que atrasa um sinal discreto e plota tanto o sinal original quanto o atrasado
# e função de média movel que usa o sinal atrasado

import matplotlib.pyplot as plt
import numpy as np
# from sinais_elementares import impulso, degrau, rampa

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

# f1 = degrau(5)
# f1 = impulso(5)
# f1 = rampa(5)
f1 = [1, 2, 3, 4, 5, 6, 4, 3, 8]
# n = np.arange(50)
# f1 = np.cos(n*np.pi/8)
a1 = atraso(f1, 2)
print("Sinal: ", f1)
print("Sinal atrasado: ", a1)

# n = np.arange(len(f1))
n = np.arange(-2, len(f1)-2) # para alinhar o gráfico do sinal atrasado
fig, ax = plt.subplots(2, 1) # uma coluna e duas linhas

ax[0].set_title('Sinal original')
ax[1].set_title("Sinal atrasado")
ax[0].stem(n, f1, linefmt="red") 
ax[1].stem(n, a1, linefmt="blue")  

plt.xticks(n) # plot mostra todos os numeros inteiros do intervalo
plt.yticks(n) # plot mostra todos os numeros inteiros do intervalo
plt.show()

