import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Especificações
fs = 10000           
fc = 1000             
M = 21                
half = M // 2

omega_c = 2 * np.pi * fc / fs  

# hd[n]
n = np.arange(-half, half + 1)
hd = np.zeros_like(n, dtype=float)
nz = n != 0
hd[nz] = np.sin(omega_c * n[nz]) / (np.pi * n[nz])
hd[~nz] = omega_c / np.pi

# Janela Retangular
def janela_retangular(M):
    w = []
    for n in range(M):
        w.append(1.0)
    return np.array(w, dtype=float)

w = janela_retangular(M)
# w = np.ones_like(hd)   # janela retangular - biblioteca pronta
hw = hd * w
h = hw.copy()

# Resposta em frequência
w_freq, H = signal.freqz(h, worN=1024, fs=fs)
mag = 20 * np.log10(np.abs(H) + 1e-12)
phase = np.unwrap(np.angle(H))

# Sinal de teste
t = np.arange(0, 0.010, 1/fs)
x = np.sin(2 * np.pi * 600 * t)
y = np.convolve(x, h, mode="same")

# ---- FFT helper ----
def compute_fft(sinal, fs):
    N = 4096
    Xf = np.fft.rfft(sinal, n=N)
    freqs = np.fft.rfftfreq(N, d=1/fs)
    return freqs, np.abs(Xf)

freqs_x, Xf = compute_fft(x, fs)
freqs_y, Yf = compute_fft(y, fs)

print("\n========== INFORMAÇÕES DO FILTRO FIR ==========")
print(f"Taxa de amostragem (fs): {fs} Hz")
print(f"Frequência de corte (fc): {fc} Hz")

# conversão para radianos normalizada (0 a pi)
wc_rad = 2 * np.pi * fc / fs
print(f"Frequência de corte em radianos (ωc): {wc_rad:.4f} rad/amostra \n")

print("========== INFORMAÇÕES DO SINAL ==========")
print(f"Duração do sinal: {t[-1]:.6f} s")

plt.figure(figsize=(14, 9))

# Magnitude
plt.subplot(2, 2, 1)
plt.plot(w_freq, mag)
plt.axvline(fc, color='k', linestyle='--')
plt.title("Resposta em Magnitude (dB)")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)

# Fase
plt.subplot(2, 2, 2)
plt.plot(w_freq, phase)
plt.title("Resposta em Fase")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Fase (rad)")
plt.grid(True)

# Sinal no tempo
plt.subplot(2, 1, 2)
plt.plot(t*1000, x, label="Entrada")
plt.plot(t*1000, y, label="Saída filtrada")
plt.title("Sinal no Tempo (Entrada x Saída)")
plt.xlabel("Tempo (ms)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

plt.plot(freqs_x, Xf, label="Entrada")
plt.plot(freqs_y, Yf, label="Saída Filtrada")

plt.title("Espectro (FFT) — Entrada vs Saída")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, fs/2)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
