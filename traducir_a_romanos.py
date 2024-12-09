def traducir_a_romano(numero, posicion):

    romanos = {
        0: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],         
        1: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],         
        2: ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],         
        3: ["", "M", "MM", "MMM"]    
    }
    return romanos[posicion][numero]    



def descomponer(numero):
    descomposicion = []
    modulo = 0
    coeficiente = 0

    while numero > 0:
        modulo = numero % 10
        descomposicion.append(modulo)   
        numero //= 10

    return descomposicion 

def traductor(lista):

    resultado_romano = []

    for posicion, numero in lista:
        if posicion == 0:
            resultado_romano.apend(traducir_a_romano(numero))
        elif posicion == 1:
            resultado_romano.apend(traducir_a_romano(numero))
        elif posicion == 2:
            resultado_romano.apend(traducir_a_romano(numero))
        elif posicion == 3:
            resultado_romano.apend(traducir_a_romano(numero))
    
    return resultado_romano