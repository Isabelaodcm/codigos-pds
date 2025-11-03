# Implementar o processo de amostragem abordado na última aula. Ou seja, dado um sinal contínuo x(t) 
# e um período de amostragem T obter o x[n] equivalente. Plote x(t), sua transformada de Fourier, 
# assim como x[n] e sua transformada de Fourier.
# Verifique que sem um filtro passa-baixa a transformada de Fourier de x[n] mantém repetições do 
# sinal no domínio da frequência.
import numpy as np
import matplotlib.pyplot as plt

def amostragem(x, T, duracao=1.0):
    """
        x: função contínua 
        T: período de amostragem (s)
        duracao: tempo total de simulação (s)
    """
    t = np.arange(0, duracao, 0.001)  # considerando a resolução de 1 ms

    #Sinal discreto
    n = np.arange(0, int(duracao / T))
    xn = x(n*T)
    return t, n, xn 

T = 0.05
x = lambda t: np.sin(np.pi * 7 * t)
t, n, xn = amostragem(x, T)

plt.figure(figsize=(10, 6))
    
plt.subplot(3, 1, 1)
plt.plot(t, x(t), 'b', label='x_c(t)')
plt.title('Sinal contínuo x_c(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
    
plt.subplot(3, 1, 2)
plt.stem(n*T, xn, basefmt=" ", linefmt='r-', markerfmt='ro', label='x[n]')
plt.title('Sinal discreto x[n] = x_c(nT)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amostras')
plt.grid(True)
    
plt.subplot(3, 1, 3)
plt.plot(t, x(t), 'b', alpha=0.5, label='x_c(t)')
plt.stem(n*T, xn, basefmt=" ", linefmt='r-', markerfmt='ro', label='x[n]')
plt.title('Amostragem')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
    
plt.tight_layout()
plt.show()