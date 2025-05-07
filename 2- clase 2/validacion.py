valor = float(input("Ingrese un valor positivo: "))

while valor < 0:
    valor = float(input("Valor incorrecto. Ingrese un valor positivo: "))

print(f"El valor es {valor}")