# Funçao para resolver fraçoes parciais

# from sympy import symbols, apart

# # Definir as variáveis
# z = symbols('z')

# # expressao = (8*z - 19) / ((z-2)*(z-3)*z)
# # expressao = (z**2) / ((z**2)-(1.9*z)+0.9)
# expressao1 = 1 / ((1-z**(-1))*(1-0.9*z**(-1)))

# # Decompor a fração em frações parciais
# resultado = apart(expressao)

# # Imprimir o resultado
# print(resultado)

# from scipy.signal import residuez

# # coeficientes do numerador e denominador
# b = [1.0]       # numerador
# a = [1.0, -1.9, 0.9]  # denominador (z^2 - 1.9z + 0.9)

# r, p, k = residuez(b, a)
# print("Resíduos:", r) # no numerador
# print("Polos:", p) # no denominador (z-p)
# print("Constante:", k)


def decompor_frac_parciais(a, b, numerador):
    """
    Decompõe uma fração da forma N(z) / ((z - a)*(z - b))
    Retorna A e B tais que:
        N(z)/((z - a)*(z - b)) = A/(z - a) + B/(z - b)
    
    Parâmetros:
        a, b : polos (float)
        numerador : função lambda ou callable que recebe z e retorna N(z)
    """
    # Calcula A e B
    A = numerador(a) / (a - b)
    B = numerador(b) / (b - a)

    # Retorna a expressão simbólica em string
    expr = f"{A:.4f}/(z - {a}) + {B:.4f}/(z - {b})"
    return A, B, expr

# Y(z) = z² / ((z - 1)(z - 0.9))
# 1 / ((1-z**(-1))*(1-0.9*z**(-1)))
numerador = lambda z: z**2
A, B, expr = decompor_frac_parciais(a=1, b=0.9, numerador=numerador)
print(f"A = {A:.4f}, B = {B:.4f}")
print("Frações Parciais:")
print("Y(z) =", expr)
