contador = 0
acumulador = 0

while contador < 10:
    
    contador += 1
    valor = float(input("ingrese el costo del gasto realizado: "))

    acumulador += valor

    promedio = acumulador / contador
    print(f"El promedio es {promedio}")
