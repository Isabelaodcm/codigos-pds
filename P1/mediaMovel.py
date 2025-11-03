import numpy as np;
import matplotlib.pyplot as plt

from sinal_atrasado import atraso

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