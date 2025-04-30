numero = int(input("Ingrese un número para calcular el factorial: "))

# factorial = 1

# for i in range(numero, 1, -1):
#     factorial *= i

# print(f"El factorial de {numero} es {factorial}")

def calcular_factorial(n: int) -> int:

    '''
    Retorna el producto de todos los números enteros positivos desde la unidad
    hasta el número definido.
    Recibe un entero.
    Retorna un entero.
    '''

    if n == 2:
        return 2
        
    else:
        factorial = n * calcular_factorial(n - 1)
        return factorial

print("Acá arranca recursividad")
factorial_r = calcular_factorial(numero)

print(f"El factorial de {numero} es {factorial_r}")

# existe memoria Heap y memoria Stack
