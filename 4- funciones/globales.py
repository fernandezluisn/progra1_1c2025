# variable global
divisor = 6

def dividir(dividendo: int= 12)-> int:

    global divisor

    # estoy cometiendo un ERROR en la siguiente linea
    divisor -= 2

    resultado = dividendo / divisor

    return resultado

print(f"el divisor es {divisor}")
print(dividir())
print(f"el divisor es {divisor}")
print(dividir())


def dividir(divisor, dividendo: int= 12)-> int:

    # estoy cometiendo un ERROR en la siguiente linea
    divisor -= 2

    resultado = dividendo / divisor

    return resultado

print(f"el divisor es {divisor}")
print(dividir(26))
print(f"el divisor es {divisor}")
print(dividir(26))
print(f"el divisor es {divisor}")
print(dividir(24))
print(f"el divisor es {divisor}")
print(dividir(24))
