def buscar_lineal(lista: list, buscado: any)-> int:

    '''
    Realiza una busqueda lineal sobre una lista.
    Recibe una lista y un elemento de cualquier tipo.
    Retorna un entero con el inde de la posición que ocupa el elemento.
    En caso de no encontrarlo, devuelve None.
    '''

    if type(lista) != list:
        print("La función debe recibir una lista")
        return None

    for i in range(len(lista)):

        if lista[i] == buscado:
            return i
        
    return None

def buscar_binaria(lista: list, buscado: int)->int:

    '''
    Realiza una busqueda binaria sobre una lista.
    Recibe una lista y un elemento de cualquier tipo.
    Retorna un entero con el inde de la posición que ocupa el elemento.
    En caso de no encontrarlo, devuelve None.
    '''

    if type(lista) != list:
        print("La función debe recibir una lista")
        return None

    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        mitad = (inicio + final) // 2

        if lista[mitad] == buscado:
            return mitad
        elif  buscado < lista[mitad]:
            inicio = mitad - 1
        else:
            final = mitad + 1

    return None
