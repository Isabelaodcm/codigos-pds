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
    t = np.arange(0, duracao, 0.001)  # tempo contínuo (resolução de 1 ms)
    n = np.arange(0, int(duracao / T))  # índices discretos
    xn = x(n * T)  # amostras
    return t, n, xn

fs = 20
T = 1/fs 

# x = lambda t: np.sin(2 * np.pi * 7 * t) 
x = lambda t: np.sin(np.pi * 5 * t)
# f1, f2 = 3, 8
# x = lambda t: np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)
t, n, xn = amostragem(x, T)


fs = 1 / T
# Sinal contínuo aproximado para FFT
xc = x(t)

# FFT do sinal contínuo
N_c = len(xc)
Xc = np.fft.fftshift(np.fft.fft(xc))
freq_c = np.fft.fftshift(np.fft.fftfreq(N_c, 0.001)) 

# FFT do sinal amostrado
N_d = len(xn)
Xd = np.fft.fftshift(np.fft.fft(xn, N_c))

freq_d = np.fft.fftshift(np.fft.fftfreq(N_c, T))


plt.figure(figsize=(10, 10))

plt.subplot(4, 1, 1)
plt.plot(t, xc, 'b', label='x_c(t)')
plt.title('Sinal contínuo x_c(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(4, 1, 1)
plt.stem(n * T, xn, basefmt=" ", linefmt='r-', markerfmt='ro', label='x[n]')
plt.title('Sinal amostrado x[n] = x_c(nT)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amostras')
plt.grid(True)

# Espectro do sinal contínuo
plt.subplot(4, 1, 2)
plt.plot(freq_d, np.abs(Xc) / N_c, 'b')
plt.title('TF do sinal contínuo')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

# Espectro do sinal amostrado
plt.subplot(4, 1, 3)
plt.plot(freq_d, np.abs(Xd) / N_d, 'r')
plt.title('TF do sinal amostrado')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.tight_layout()
plt.show()