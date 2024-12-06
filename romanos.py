
numeros_romanos = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "c": 100,
    "D": 500,
    "M": 1000
}

def a_romanos(valor: int) -> str:
    romano = ""
    for clave, value in numeros_romanos.items():
        if value == valor:
            romano = clave
    return romano
         



#assert a_romanos(1) == "I"
#assert a_romanos(500) == "D"

