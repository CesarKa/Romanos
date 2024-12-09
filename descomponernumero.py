

def descomponer(numero):
    descomposicion = []
    modulo = 0
    coeficiente = 0

    while numero > 0:
        modulo = numero % 10
        descomposicion.append(modulo)   
        numero //= 10

    return descomposicion 