#desarrollamos una función que recibe una lista y calcula la media
def calcular_media(notas: list):

    acumulador = 0
    contador = 0

    for i in range(len(notas)):
        acumulador += notas[i]
        contador += 1

    print(f"La media es {acumulador/contador}")

def calcular_media_2(acumulador: int, contador: int):

    return acumulador/contador

lista_notas = list(range(10))

print(lista_notas)

calcular_media(lista_notas)



    
