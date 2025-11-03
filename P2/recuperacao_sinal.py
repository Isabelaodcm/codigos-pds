# Dado um sinal discreto x[n] e um período de amostragem T, obter o x(t) equivalente.

import numpy as np
import matplotlib.pyplot as plt
f

def reconstrucao_ideal(x_n, T, t_pontos):
    """
    x_n (array): Sequência de amostras do sinal (x[n]).
    T (float): Período de amostragem (T).
    t_pontos (array): Pontos de tempo 't' onde o sinal reconstruído será calculado.

    """
    
    M = len(x_n)
    x_r_t = np.zeros_like(t_pontos, dtype=float)
    
    # Percorre o índice das amostras (n)
    for n in range(M):
        # 1. Calcula o argumento para a função sinc: (t - nT) / T
        argumento_sinc = (t_pontos - n * T) / T
        
        # 2. Calcula a função sinc h_r(t - nT) = sen(pi*x)/(pi*x) onde x = argumento_sinc
        h_r_t_menos_nT = np.sinc(argumento_sinc)
        
        # 3. Acumula a soma do produto da amostra x[n] pela sinc deslocada
        x_r_t += x_n[n] * h_r_t_menos_nT
        
    return x_r_t

# Parâmetros
f0 = 1.0          # Frequência do sinal original (1 Hz)
T = 0.1           # Período de amostragem (Ts = 0.1s, fs = 10Hz). Cita-se fs > 2*f0 (2Hz), então OK.
tempo_final = 2.0 # Duração do sinal

# 1. Geração do Sinal Contínuo Original (xc(t))
t_original = np.linspace(0, tempo_final, 500)
x_c_t = np.cos(2 * np.pi * f0 * t_original) 

# 2. Amostragem: Cria a sequência de amostras x[n] = xc(nT)
n_amostras = np.arange(0, tempo_final / T + 1) # Garante que inclui o último ponto
t_amostras = n_amostras * T
x_n = np.cos(2 * np.pi * f0 * t_amostras) 

# 3. Reconstrução: Define os pontos de tempo contínuo para calcular x_r(t)
t_pontos_rec = np.linspace(0, tempo_final, 500)

# 4. Aplica a função de reconstrução ideal
x_r_t = reconstrucao_ideal(x_n, T, t_pontos_rec)


plt.figure(figsize=(12, 6))

# Plota o sinal original (Ideal)
plt.plot(t_original, x_c_t, label='$x_c(t)$ - Sinal Contínuo Original', color='blue', linewidth=2, linestyle='--')

# Plota as amostras (x[n])
plt.stem(t_amostras, x_n, linefmt='r-', markerfmt='ro', basefmt=' ', label='Amostras $x[n]$')

# Plota o sinal reconstruído (xr(t))
plt.plot(t_pontos_rec, x_r_t, label='$x_r(t)$ - Sinal Reconstruído (Interpolação Sinc)', color='green', linewidth=1.5)

# Configurações do Gráfico
plt.title(f'Reconstrução Ideal de um Sinal Cosseno (f0={f0} Hz, Ts={T} s)')
plt.xlabel('Tempo (t) [s]')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.tight_layout()
plt.show()