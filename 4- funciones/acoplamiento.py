# variable global
divisor = 6

def dividir(dividendo: int= 12)-> int:

    #referencia
    global divisor

    # estoy cometiendo un ERROR en la siguiente linea
    divisor -= 2

    resultado = dividendo / divisor

    return resultado

# versión incorrecta de promediar, acoplada a dividir 
# a través de la variable global
def promediar_acoplada(acumulador: int)->float:

    global divisor

    resultado = acumulador / divisor

    return resultado

def promediar_sin_acoplar(acumulador: int,
                          divisor: int)->float:    

    resultado = acumulador / divisor

    return resultado

print(dividir(26))

# Estoy suponiendo que el promedio va a ser entre 6 casos
print(promediar_acoplada(10))

