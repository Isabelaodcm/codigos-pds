# Aula 19/09/2025 Processamento digital de sinais
# Funções para plotar sinais impulso, degrau e rampa

def impulso(n): 
    valores = []
    # for valor in range(2*n+1):
    for valor in range(-n, n+1):
        if valor == 0:  
            valores.append(1)
        
        else:
            valores.append(0)

    return valores

# print(impulso(1))
# print(impulso(3))

def degrau(n):
    valores = []
    for valor in range(-n, n+1):
        if valor <0:
            valores.append(0)

        else:
            valores.append(1)

    return valores

# print(degrau(3))

def rampa(n):
    valores = []
    for valor in range(-n, n+1):
        if valor <0:
            valores.append(0)
        
        else:
            valores.append(valor)

    return valores

# print(rampa(4))

