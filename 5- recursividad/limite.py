def imprimir_numero(n:int):

    if n > int(-996):
        imprimir_numero(n - 1)

        print(n)

imprimir_numero(0)