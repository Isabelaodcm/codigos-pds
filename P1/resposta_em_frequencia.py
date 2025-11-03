import numpy as np
import matplotlib.pyplot as plt

def resposta_frequencia(b, a, num_pontos=1024, omega_range=(-2*np.pi, 3*np.pi)):
    """
    b: coeficientes do numerador
    a: coeficientes do denominador
    num_pontos: resolução da frequência
    omega_range: intervalo de frequência (rad)

    Imprime:
    - H(z)
    - |H(e^{jΩ})|
    - ∠H(e^{jΩ}) com tan⁻¹ se aplicável
    Retorna:
    - omega, amplitude, fase
    """

    def expressao_em_e_jomega(coefs, nome):
        termos = []
        for i, c in enumerate(coefs):
            if c == 0:
                continue
            termo = f"{c:.3g}"
            if i > 0:
                termo += f"·e^(-j{i}Ω)"
            termos.append(termo)
        return f"{nome}(e^(-jΩ)) = " + " + ".join(termos) if termos else f"{nome}(e^(-jΩ)) = 0"

    def polinomio_em_z_inverso(coefs):
        termos = []
        for i, c in enumerate(coefs):
            if c == 0:
                continue
            termo = f"{c:.3g}"
            if i > 0:
                termo += f"·z^(-{i})"
            termos.append(termo)
        return " + ".join(termos) if termos else "0"

    def expressao_fase_tan_inv(a):
        if len(a) == 2 and a[0] == 1:
            a1 = a[1]
            sinal = '+' if a1 >= 0 else '-'
            a1_abs = abs(a1)
            return f"∠H(e^{{jΩ}}) = -tan⁻¹[({a1_abs}·sin(Ω)) / (1 {sinal} {a1_abs}·cos(Ω))]"
        else:
            return f"∠H(e^{{jΩ}}) = arg(B(e^(-jΩ))) - arg(A(e^(-jΩ)))"

    # Imprime H(z)
    num_str = polinomio_em_z_inverso(b)
    den_str = polinomio_em_z_inverso(a)
    print(f"H(z) = ({num_str}) / ({den_str})")

    # Imprime forma simbólica da amplitude e fase
    B_str = expressao_em_e_jomega(b, "B")
    A_str = expressao_em_e_jomega(a, "A")
    print(B_str)
    print(A_str)
    print(f"|H(e^{{jΩ}})| = |B(e^(-jΩ)) / A(e^(-jΩ))|")
    print(expressao_fase_tan_inv(a))

    # Calcula resposta em frequência
    omega = np.linspace(omega_range[0], omega_range[1], num_pontos)
    z = np.exp(1j * omega)
    B = np.polyval(b, z**-1)
    A = np.polyval(a, z**-1)
    H = B / A
    amplitude = np.abs(H)
    fase = np.angle(H)

    return omega, amplitude, fase


# Exemplo: H(z) = 1 / (1 - 0.8z^-1)
b = [1]
a = [1, -0.8]

omega, amp, fase = resposta_frequencia(b, a)

# Plotando
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(omega, amp)
plt.title("Amplitude |H(e^{jω})|")
plt.xlabel("Frequência (rad)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(omega, fase)
plt.title("Fase ∠H(e^{jω})")
plt.xlabel("Frequência (rad)")
plt.grid(True)

plt.tight_layout()
plt.show()
