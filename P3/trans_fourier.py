import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal

fs = 1000          # frequência de amostragem (Hz)
T = 1              # duração do sinal (s)
t = np.linspace(0, T, fs, endpoint=False)

f0 = 10            # frequência do cosseno (Hz)

# Sinais
x = 3 * np.cos(2 * np.pi * f0 * t)   # sinal original
xr = x + 5                           # sinal com DC offset

# Função FFT

def fft_sinal(sinal, fs):
    N = len(sinal)
    X = np.fft.fft(sinal)
    X = np.fft.fftshift(X)
    freqs = np.fft.fftfreq(N, 1/fs)
    freqs = np.fft.fftshift(freqs)
    return freqs, np.abs(X) / N

# FFTs
freq_x, X_f = fft_sinal(x, fs)
freq_xr, Xr_f = fft_sinal(xr, fs)


# (a) x(t) — tempo e frequência
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(t, x)
plt.title("x(t) no tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(1, 2, 2)
plt.stem(freq_x, X_f)
plt.title("Espectro de x(t)")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.xlim(-50, 50)
plt.grid()

plt.tight_layout()
plt.show()

# (b) xr(t) — tempo e frequência

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(t, xr)
plt.title("xr(t) no tempo (com DC offset)")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(1, 2, 2)
plt.stem(freq_xr, Xr_f)
plt.title("Espectro de xr(t)")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.xlim(-50, 50)
plt.grid()

plt.tight_layout()
plt.show()

# (c) Remoção da média

media_xr = np.mean(xr)
xr_sem_dc = xr - media_xr

freq_xr_sem_dc, Xr_sem_dc_f = fft_sinal(xr_sem_dc, fs)

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(t, xr_sem_dc)
plt.title("xr(t) após remoção da média")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(1, 2, 2)
plt.stem(freq_xr_sem_dc, Xr_sem_dc_f)
plt.title("Espectro após remoção da média")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.xlim(-50, 50)
plt.grid()

plt.tight_layout()
plt.show()

# (d) Remoção do DC usando filtro passa-altas (domínio da frequência)

# FFT do sinal com DC
Xr = np.fft.fft(xr)
freqs = np.fft.fftfreq(len(xr), 1/fs)

# Filtro passa-altas ideal: remove DC (frequência 0)
Xr_filtrado = Xr.copy()
Xr_filtrado[freqs == 0] = 0   # zera a componente DC

# Retorno ao domínio do tempo
xr_filtrado = np.real(np.fft.ifft(Xr_filtrado))

# FFT do sinal filtrado (para visualização)
freq_xr_filtrado, Xr_filtrado_f = fft_sinal(xr_filtrado, fs)

# Gráficos
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(t, xr_filtrado)
plt.title("xr(t) após filtro passa-altas (remoção do DC)")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(1, 2, 2)
plt.stem(freq_xr_filtrado, Xr_filtrado_f)
plt.title("Espectro após filtro passa-altas")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.xlim(-50, 50)
plt.grid()

plt.tight_layout()
plt.show()


# (e) Comparação no tempo: sinal original x(t) vs sinal filtrado

plt.figure(figsize=(10, 4))

plt.plot(t, x, label="x(t) original", linewidth=2)
plt.plot(t, xr_filtrado, '--', label="x(t) após filtro passa-altas", linewidth=2)

plt.title("Comparação entre sinal original e sinal filtrado")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

