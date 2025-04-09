valor = int(input("Ingrese el valor de una deuda: "))

while valor > 0:
    print("Error, está trabajando con deudas, el valor debe ser negativo.")
    valor = int(input("Ingrese el valor de una deuda: "))

print(f"La deuda es de {valor}")