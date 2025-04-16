def dividir(dividendo, divisor):
    if dividendo != 0 and divisor != 0:
        resultado = dividendo / divisor
        print(f"El resultado es {resultado}")
    else:
        print("El dividendo y el divisor deben ser distintos de 0")

dividendo = float(input("¿Cuál es el dividendo? "))
divisor = float(input("¿Cuál es el divisor? "))

dividir(dividendo, divisor)
dividir(4, 2)
dividir(3, 2)
dividir(7, 3)