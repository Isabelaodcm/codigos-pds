# Aula 22/09 PDS - funcao para plotar a resposta da saolucao de uma edo de 1° grau

import matplotlib.pyplot as plt
import numpy as np

tau = 1
k = 0
v0 = 5

a=-1/tau
b=-k/tau

c = v0 - k

t = np.arange(50)
at = np.multiply(a,t)
y = (b/a) + np.multiply(c, np.exp(at))

plt.plot(t,y)
plt.show()