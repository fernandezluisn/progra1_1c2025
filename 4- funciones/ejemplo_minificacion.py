#desarrollamos una función que recibe una lista y calcula la media
def calcular_media(notas: list):

    bandera = True
    maximo = 0

    acumulador = 0
    contador = 0

    for i in range(len(notas)):
        acumulador += notas[i]
        contador += 1

        # esto no es correcto, la función debe realizar una sola tarea
        if bandera:
            maximo = notas[i]
        elif notas[i] > maximo:
            maximo = notas[i]



    print(f"La media es {acumulador/contador}")

# SI queremos calcular máximo, lo hacemos en una función separada de la media
def calcular_maximo(notas: list):

    bandera = True

    for i in range(len(notas)):
        # esto no es correcto, la función debe realizar una sola tarea
        if bandera:
            maximo = notas[i]
        elif notas[i] > maximo:
            maximo = notas[i]

    print(f"El máximo es {maximo}")