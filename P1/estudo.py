# Estudo: script para plotar um grafico com o valor do sinal em determinado instante a destacado
import numpy as np
import matplotlib.pyplot as plt

# # Função qualquer
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

array1 = [[(-3)**(-1), -(-3)**(-1)], [(-3)**(-2), -2*((-3)**(-2))]]
array2 = [-1/3, -2/9]

# numpy.linspace(start, stop, num=50, endpoint=True):
# start: O valor inicial da sequência (obrigatório).
# stop: O valor final da sequência (obrigatório).
# num: O número de amostras a serem geradas. Se omitido, o padrão é 50.
# endpoint: Se True (padrão), o valor stop é incluído no array. Se False, o valor stop é excluído. 