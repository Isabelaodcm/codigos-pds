# Implemente um programa para resolver a resposta a entrada nula de um sistema discreto linear e 
# invariante no tempo – slide 32/54 (Aula_4_-_Equacoes_a_diferenca.pdf).
# O programa recebe como entrada os coeficientes de y, as condições iniciais e um vetor de índices 
# (n), sendo que tem como saída os gamas, c1 e c2, assim como plota a solução final 
# y0 (solução homogênea). Adicionalmente, informe se o sistema é estável ou instável.
import math 
import numpy as np
import matplotlib.pyplot as plt

c = [-0.6, -0.16]
ci = [0, (25 / 4)]
n = np.arange(0,30)
def solucao_geral(coeficientes, ci, n):
    # considerando que a ordem é igual a 2
    delta = (coeficientes[0])**2 - (4*1*coeficientes[1])
    gama1 = (-coeficientes[0] + math.sqrt(delta))/2
    gama2 = (-coeficientes[0] - math.sqrt(delta))/2
        
    print(f"gama1: {gama1} \ngama2: {gama2}")

    array1 = np.array([[gama1**(-1), gama2**(-1)], [gama1**(-2), gama2**(-2)]])
    array2 = np.array([ci[0], ci[1]])

    constantes = np.linalg.solve(array1, array2) # funcao q resolve sistemas lineares
    c1 = constantes[0]
    c2 = constantes[1]
    print(f"c1: {constantes[0]:.2f} \nc2: {constantes[1]:.2f}")
    
    y0 = c1*(gama1)**n + c2*(gama2)**n
    print(f"Solução geral: {c1:.2f}({gama1})^n + {c2:.2f}({gama2})^n")
    return y0

solucao = solucao_geral(c, ci, n)
plt.stem(n, solucao)
plt.show()


# if len(coef) == 2:
#     coef1 = coef[0]
#     coef1*gama + coef[1] = 0 
#     resolve eq do 1 grau

# if len(coef) == 3:
#     coef[0]*gama^2 + coef[1]*gama + coef1[2]
#     calculo baskhara

#     if baskhara >= 0:
#         resolve normal

#     else:
#         resolve para raizes complexas
    
