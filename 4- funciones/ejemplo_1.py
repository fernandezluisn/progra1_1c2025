#desarrollamos una función que recibe una lista y calcula la media
def calcular_media(notas: list) -> float:

    acumulador = 0
    contador = 0

    for i in range(len(notas)):
        acumulador += notas[i]
        contador += 1

    media_funcion = acumulador/contador
    print(f"La media es {media_funcion}")

    return media_funcion

def calcular_media_2(acumulador: int, contador: int):

    return acumulador/contador

lista_notas = list(range(10))

print(lista_notas)

media_global = calcular_media(lista_notas)

print(media_global)



    
