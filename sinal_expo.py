# Só um teste de plot de um sinal exponencial 
import matplotlib.pyplot as plt
import numpy as np

n = np.arange(50)
j = 1j 
# f1 = np.exp((2+j*3)*n)
f1 = (0.9)**n

plt.stem(n, f1)
plt.show()