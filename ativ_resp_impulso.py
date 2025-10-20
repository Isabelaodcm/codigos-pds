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

# Modelar o processo de geração do sinal metabólico cerebral como um sistema Linear e Invariante no Tempo (LTI)
#  é vantajoso porque simplifica significativamente a análise e o entendimento do fenômeno. Um sistema LTI pode ser 
# descrito apenas por sua resposta ao impulso, permitindo que a relação entre a entrada e a saída seja expressa por
#  uma simples convolução. Isso torna possível aplicar ferramentas matemáticas, como as transformadas de Fourier, 
# Laplace e Z, para analisar o comportamento do sistema em diferentes frequências. 
# Além disso, a linearidade garante que a resposta a uma combinação de estímulos seja a soma das respostas 
# individuais, facilitando a previsão do comportamento frente a estímulos complexos. A invariância no tempo 
# assegura que as propriedades do sistema não mudam com o tempo, o que torna o modelo estável e reprodutível. Assim, 
# representar o processo como um sistema LTI permite ao cientista analisar e interpretar os sinais cerebrais de 
# forma mais simples, eficiente e com boa aproximação do comportamento real.