# Estudo: script para plotar um grafico com o valor do sinal em determinado instante a destacado
import numpy as np
import matplotlib.pyplot as plt

# Função qualquer
def f(t):
    return np.sin(t) + t**2

n = np.arange(50)
f1 = np.sin(n) + n**2
# Propriedade do peneiramento: f(a)
a = 20.0
fa = f(a)
print("Valor de f(a):", f(a))

# basefmt: tira a linha vermelha que aparece quando eu faço o scatter
# zorder: define o tamanho do circulo vermelho
# linefmt: define o a cor do grafico
plt.stem(n, f1, linefmt="-b", basefmt=" ")
plt.scatter(a, fa, color="red", s=50, zorder=5, label=f"f({a}) = {fa:.2f}")
plt.legend()
plt.show()