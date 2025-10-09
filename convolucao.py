# Código para implementar a função de convolução
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

x = [0.8, 0.3, 0.5, 0.7, 1.3]
# h = 0.5**n
h = [1, 0.5, 0.25, 0.125, 0.0625]

print(np.convolve(x, h))

c1 = convolucao(x, h)
n = np.arange(len(c1))
print("convolucao: ", c1)

fig, axs = plt.subplots(3, 1)
axs[0].stem(np.arange(len(x)), x, label = "x[n]")
axs[1].stem(np.arange(len(h)), h, label = "h[n]")
axs[2].stem(n, c1, label = "Convolução")

for l in axs:
    l.grid(True)
    l.legend()

plt.legend()  
plt.show()


    