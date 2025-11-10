import numpy as np
import matplotlib.pyplot as plt

def filtro_passa_baixa(fc, f_sinal, amplitude=1, fase=0):
    """
    fc: frequência de corte (Hz)
    f_sinal: frequência do sinal de entrada (Hz)
    amplitude: amplitude do sinal de entrada
    fase: fase do sinal de entrada (em graus)
    """
    # Frequência angular de corte
    wc = 2 * np.pi * fc

    # Frequências de análise (em Hz)
    f_min = max(0.1, min(fc, f_sinal) / 10)
    f_max = max(fc, f_sinal) * 100
    f = np.logspace(np.log10(f_min), np.log10(f_max), 800)
    w = 2 * np.pi * f

    # Função de transferência H(jw)
    H = 1 / (1 + 1j * (w / wc))

    # Módulo e fase (em graus)
    H_mod = np.abs(H)
    H_fase = np.angle(H, deg=True)
    mag_dB = 20 * np.log10(H_mod * amplitude)
    fase_total = H_fase + fase

    # Cálculo da amplitude e fase para o f_sinal
    w_sinal = 2 * np.pi * f_sinal
    H_sinal = 1 / (1 + 1j * (w_sinal / wc))
    ganho_sinal = np.abs(H_sinal)
    fase_sinal = np.angle(H_sinal, deg=True)

    print(f"Frequência do sinal: {f_sinal} Hz")
    print(f"Amplitude do sinal após o filtro: {ganho_sinal * amplitude:.4f}")
    print(f"Fase do sinal após o filtro: {fase_sinal:.2f}°")

    # ---- PLOTAGEM ----
    plt.figure(figsize=(10, 14))

    # 1. Módulo da Função de Transferência
    plt.subplot(5, 1, 1)
    plt.plot(f, H_mod, color='blue')
    plt.axvline(fc, color='g', linestyle='--', label=f'f_corte = {fc} Hz')
    plt.axvline(f_sinal, color='r', linestyle='--', label=f'f_sinal = {f_sinal} Hz')
    plt.xscale('log')
    plt.title('Função de Transferência |H(jω)| (em Hz)')
    plt.ylabel('|H(jω)|')
    plt.grid(True, which='both', ls='--')
    plt.legend()

    # 2. Fase da Função de Transferência
    plt.subplot(5, 1, 2)
    plt.plot(f, H_fase, color='orange')
    plt.axvline(fc, color='g', linestyle='--')
    plt.axvline(f_sinal, color='r', linestyle='--')
    plt.xscale('log')
    plt.ylabel('Fase H(jω) (graus)')
    plt.grid(True, which='both', ls='--')

    # 3. Diagrama de Bode - Magnitude (dB)
    plt.subplot(5, 1, 3)
    plt.semilogx(f, mag_dB, label='Magnitude (dB)', color='purple')
    plt.axvline(fc, color='g', linestyle='--')
    plt.axvline(f_sinal, color='r', linestyle='--')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True, which='both', ls='--')
    plt.legend()

    # 4. Diagrama de Bode - Fase (graus)
    plt.subplot(5, 1, 4)
    plt.semilogx(f, fase_total, label='Fase (graus)', color='brown')
    plt.axvline(fc, color='g', linestyle='--')
    plt.axvline(f_sinal, color='r', linestyle='--')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Fase (graus)')
    plt.grid(True, which='both', ls='--')
    plt.legend()

    # sinal original vs filtrado
    t = np.linspace(0, 3 / f_sinal, 1000)
    x_in = amplitude * np.sin(2 * np.pi * f_sinal * t + np.deg2rad(fase))
    x_out = ganho_sinal * amplitude * np.sin(2 * np.pi * f_sinal * t + np.deg2rad(fase + fase_sinal))

    plt.subplot(5, 1, 5)
    plt.plot(t, x_in, label='Sinal Original', color='blue')
    plt.plot(t, x_out, label='Sinal Filtrado', color='red', linestyle='--')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.title('Comparação no Tempo')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

filtro_passa_baixa(fc=500, f_sinal=100, amplitude=1)
