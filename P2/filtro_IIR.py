import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#  PARÂMETROS
# fs = 1                 
fs = 10000                 # Hz (frequência de amostragem)
Td = 1/fs                  # período de amostragem

# Frequências em tempo discreto (rad)
# wp = 0.2*np.pi             # faixa de passagem (1000 Hz)
# ws = 0.3*np.pi             # faixa de rejeição (1500 Hz)

wp_hz = 1000     # frequência de corte em Hz
ws_hz = 1500     # frequência de rejeição em Hz

# Conversão para radianos discretos - frquencia digital normalizada
wp = 2*np.pi*(wp_hz / fs)     # radianos (ω = 2π f / fs)
ws = 2*np.pi*(ws_hz / fs)

# Ganhos especificados no slide 15/32
Ap = 0.89125               # mínimo da banda de passagem
As = 0.17783               # máximo na banda de rejeição


# 1) CONVERTER ESPECIFICAÇÕES DISCRETAS PARA CONTÍNUAS
#    Relação:  Ω = ω / Td    (slide 9 e slide 14)

Wp = wp / Td               # rad/s
Ws = ws / Td               # rad/s


# 2) CALCULAR ORDEM N E FREQUÊNCIA DE CORTE Ωc DO BUTTERWORTH
#    |H(jΩ)|^2 = 1 / (1 + (Ω/Ωc)^(2N)) - slides 16 e 17

def solve_N_Omegac(Wp, Ws, Ap, As):
    Rp = (1/Ap)**2 - 1
    Rs = (1/As)**2 - 1

    N = np.log(Rs/Rp) / (2*np.log(Ws/Wp))
    N = int(np.ceil(N))  # ordem inteira

    # recalcular Ωc usando banda de passagem
    Omegac = Wp / (Rp**(1/(2*N)))

    return N, Omegac

gpass = -20*np.log10(Ap)    # ripple em dB
gstop = -20*np.log10(As)    # atenuação em dB

# N, Omegac = signal.buttord(Wp, Ws, gpass, gstop, analog=True) # cálculo usando funcao pronta

N, Omegac = solve_N_Omegac(Wp, Ws, Ap, As)
print("Ordem N =", N)
print("Ωc =", Omegac/fs)


# 3) PROJETAR FILTRO BUTTERWORTH ANALÓGICO (CONTÍNUO)

b_an, a_an = signal.butter(N, Omegac, btype='low', analog=True)

# 4) TRANSFORMAR PARA DISCRETO — INVARIÂNCIA AO IMPULSO

bd, ad, dt = signal.cont2discrete((b_an, a_an), Td, method='impulse')
bd = bd.flatten()

# 5) RESPOSTA EM FREQUÊNCIA (COMPARAÇÃO COM SLIDE 20)
w, h = signal.freqz(bd, ad, worN=2048)

plt.figure(figsize=(12,5))


# MAGNITUDE EM dB
plt.subplot(1,2,1)
plt.plot(w, 20*np.log10(abs(h)), label='|H(e^{jw})| (dB)')
plt.axvline(wp, color='green', linestyle='--', label='ωp')
plt.axvline(ws, color='red', linestyle='--', label='ωs')

# Linhas horizontais gpass e gstop
plt.axhline(-gpass, color='orange', linestyle='--', label=f"-gpass = -{gpass:.2f} dB")
plt.axhline(-gstop, color='purple', linestyle='--', label=f"-gstop = -{gstop:.2f} dB")

plt.title("Magnitude (dB)")
plt.xlabel("Frequência (rad/amostra)")
plt.ylabel("Magnitude (dB)")
plt.legend()
plt.grid()

# ============================
# MAGNITUDE LINEAR
# ============================
plt.subplot(1,2,2)
plt.plot(w, abs(h), label='|H(e^{jw})|')
plt.axvline(wp, color='green', linestyle='--', label='ωp')
plt.axvline(ws, color='red', linestyle='--', label='ωs')

# Em linear, Ap e As também podem ser mostrados
plt.axhline(Ap, color='orange', linestyle='--', label=f"Ap = {Ap:.2f}")
plt.axhline(As, color='purple', linestyle='--', label=f"As = {As:.2f}")

plt.title("Magnitude (linear)")
plt.xlabel("Frequência (rad/amostra)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid()

plt.show()


# 6) TESTAR FILTRO COM DIFERENTES SINAIS

t = np.arange(0, 0.01, 1/fs)

sinal_low = np.cos(2*np.pi*1500*t)      # antes da faixa de corte
sinal_high = np.sin(2*np.pi*3000*t)    # depois da faixa de corte
sinal_mix = sinal_low + sinal_high     # combinado

# Filtragem
y_low = signal.lfilter(bd, ad, sinal_low)
y_high = signal.lfilter(bd, ad, sinal_high)
y_mix = signal.lfilter(bd, ad, sinal_mix)


# 7)ENTRADA vs SAÍDA (item b)

plt.figure(figsize=(12,6))
# plt.plot(t, sinal_high, label="Entrada")
plt.plot(t, sinal_low, label="Entrada")
# plt.plot(t, sinal_mix, label="Entrada")
plt.plot(t, y_mix, label="Saída filtrada")
plt.title("Entrada x Saída")
plt.legend()
plt.grid()
plt.show()

# 8) RESPOSTA AO IMPULSO (item c)
imp = np.zeros(300)
imp[0] = 1
h_n = signal.lfilter(bd, ad, imp)

plt.figure(figsize=(10,4))
plt.stem(h_n)
plt.title("Resposta ao impulso h[n] — Discreta")
plt.grid()
plt.show()