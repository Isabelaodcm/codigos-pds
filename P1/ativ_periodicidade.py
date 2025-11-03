# Aula sexta 26/09 - periodicidade de sinais contínuos e discretos

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(50)
f1 = np.pi/4
print(f1)

f2 = 3*np.pi/8
print(f2)

# nesse caso x[n] é um sinal discreto
# sinal = np.cos(n*(np.pi/4))
sinal = np.cos(n*f2) # sinal com a frequencia maior, mas o período aumentou

# sinal2 = np.cos(n*np.pi*0.1)
sinal3 = np.cos(n*np.pi*0.9)
sinal4 = np.cos(n*np.pi*1.5)

fig, ax = plt.subplots(1, 2) # uma linha e duas colunas
# plt.stem(n, sinal) 

ax[0].stem(n, sinal3, linefmt="red") 
ax[1].stem(n, sinal4, linefmt="blue") 
plt.show()