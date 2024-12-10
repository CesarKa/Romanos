def traducir_a_romano(numero, posicion):

    romanos = {
        0: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],         
        1: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],         
        2: ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],         
        3: ["", "M", "MM", "MMM"]    
    }
    return romanos[posicion][numero]    


def traductor(lista):

    resultado_romano = []

    for posicion, numero in enumerate(lista):
        if posicion == 0:
            resultado_romano.append(traducir_a_romano(numero, 0))
        elif posicion == 1:
            resultado_romano.append(traducir_a_romano(numero, 1))
        elif posicion == 2:
            resultado_romano.append(traducir_a_romano(numero, 2))
        elif posicion == 3:
            resultado_romano.append(traducir_a_romano(numero, 3))
    resultado_romano.reverse()
    return "".join(resultado_romano)

def descomponer(numero):
    descomposicion = []

    while numero > 0:
        modulo = numero % 10
        descomposicion.append(modulo)   
        numero //= 10
    return descomposicion 

numero = int(input("Número que transformar: "))

lista_descompuesta = descomponer(numero)

numero_romano = traductor(lista_descompuesta)

print(f"Número romano: {numero_romano}")
