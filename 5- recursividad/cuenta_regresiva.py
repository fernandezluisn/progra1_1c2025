numero = int(input("Ingrese un número para iniciar la cuenta regresiva: "))

for i in range(numero, -1, -1):
    print(i)

def contar_regresivamente(n: int) -> None:

    '''
    Cuenta regresivamente
    Recibe un entero
    No retorna nada
    '''

    if n == (-1):
        print("Finalizó")
    else:
        print(n)
        contar_regresivamente(n - 1)

print("Acá arranca recursividad")
contar_regresivamente(numero)