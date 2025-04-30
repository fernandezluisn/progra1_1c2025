def dividir(divisor, dividendo: int= 12)-> int:    

    resultado = dividendo / divisor

    return resultado

# simulo pasaje por valor, en python todo se pasa por referencia
print(dividir(24))