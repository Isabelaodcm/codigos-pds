import numpy as np
import matplotlib.pyplot as plt

def filtro_passa_alta(tau):
    """
    Calcula a resposta em frequência de um filtro RC passa-alta.

    Parâmetros:
        R (float): resistência (ohms)
        C (float): capacitância (farads)

    Retorna:
        f (array): vetor de frequências
        H (array): resposta complexa do filtro
    """
    f = np.logspace(1, 6, 1000)   # 10 Hz a 1 MHz
    w = 2 * np.pi * f
    H = (1j * w * tau) / (1 + 1j * w * tau)
    return f, H


def plotar_bode_passa_alta(tau):
    """
    Plota o diagrama de Bode para o filtro passa-alta RC.
    """
    f, H = filtro_passa_alta(tau)
    fc = 1 / (2 * np.pi * tau)  # frequência de corte

    plt.figure(figsize=(10, 6))

    # --- Magnitude ---
    plt.subplot(2, 1, 1)
    plt.semilogx(f, 20 * np.log10(np.abs(H)))
    plt.axvline(fc, color='red', linestyle='--', label=f"f_c = {fc:.2f} Hz")
    plt.title("Filtro Passa-Alta RC - Magnitude")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True, which="both", ls="--")
    plt.legend()

    # --- Fase ---
    plt.subplot(2, 1, 2)
    plt.semilogx(f, np.angle(H, deg=True))
    plt.axvline(fc, color='red', linestyle='--')
    plt.title("Filtro Passa-Alta RC - Fase")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Fase (graus)")
    plt.grid(True, which="both", ls="--")

    plt.tight_layout()
    plt.show()


# Exemplo de uso:
# R = 1e3      # 1 kΩ
# C = 1e-6     # 1 μF

tau = 10
plotar_bode_passa_alta(tau)
