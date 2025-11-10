import numpy as np
import matplotlib.pyplot as plt

def amostragem(x, T, duracao=1.0):
    """
    x: função contínua
    T: período de amostragem (s)
    duracao: tempo total de simulação (s)
    """
    t = np.arange(0, duracao, 0.001)  # tempo contínuo (resolução de 1 ms)
    n = np.arange(0, int(duracao / T))
    xn = x(n * T)
    return t, n, xn


def reconstruir_sinal(n, xn, T, t):
    xr = np.zeros_like(t)
    for k in range(len(n)):
        xr += xn[k] * np.sinc((t - n[k]*T) / T)
    return xr


def x(t):
    return np.sin(np.pi * 5 * t)


T = 0.05
duracao = 1.0

t, n, xn = amostragem(x, T, duracao)
xr = reconstruir_sinal(n, xn, T, t)

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(t, x(t), 'b', label='x(t) original')
plt.stem(n*T, xn, linefmt='r-', markerfmt='ro', basefmt=' ', label='x[n] amostrado')
plt.plot(t, xr, 'g--', label='x_r(t) reconstruído')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Amostragem e Reconstrução do Sinal')
plt.legend()
plt.grid(True)
plt.show()