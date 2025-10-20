# funcao para calcular H[z] dada a equacao de diferenca - AULA 5 slide 28

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, apart

x = symbols('x')
fracao_parcial = x**2/(x**2 -1.9*x + 0.9)

# Parâmetros do sistema
a = 0.8                # Coeficiente da equação
N = 20                 # Número de amostras
x = np.zeros(N)        # Entrada: impulso unitário
x[0] = 1               # δ[n]

# Inicializa saída
y = np.zeros(N)

# Aplica a equação de diferença
for n in range(N):
    if n == 0:
        y[n] = x[n]    # y[0] = x[0], pois y[-1] não existe
    else:
        y[n] = a * y[n - 1] + x[n]

# Plotando a resposta ao impulso
plt.stem(range(N), y)
plt.title('Resposta ao Impulso h[n]')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.grid(True)
plt.show()
