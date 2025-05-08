from .otras_funciones import recortar_lista

def devolver_interseccion(lista_1:list, lista_2:list)-> list:

    '''
    Acá va documentación
    '''

    if len(lista_1) > len(lista_2):
        maximo = len(lista_2)
    else:
        maximo = len(lista_1)

    lista_retorno = [False] * maximo

    indice_retorno = 0

    for i in range(len(lista_1)):


        for j in range(len(lista_2)):

            if lista_1[i] == lista_2[j]:
                lista_retorno[indice_retorno] = lista_1[i]
                indice_retorno += 1
                break

    lista_retorno = recortar_lista(lista_retorno)


    return lista_retorno

def retornar_union(lista_1:list, lista_2:list)->list:

    '''
    documentación
    '''

    maximo = len(lista_1) + len(lista_2)

    #creamos lista nueva
    lista_retorno = [False] * maximo

    # suponemos que no hay valores repetidos dentro de cada lista
    for i in range(len(lista_1)):
        lista_retorno[i] = lista_1[i]

    indice_retorno = len(lista_1)

    for i in range(len(lista_2)):
        
        bandera = False

        for j in range(len(lista_1)):

            if lista_1[j] == lista_2[i]:
                bandera = True
                break
        
        if bandera == False:
            lista_retorno[indice_retorno] = lista_2[i]            
            indice_retorno += 1

    lista_retorno = recortar_lista(lista_retorno)

    return lista_retorno

def retornar_diferencia(lista_1:list, lista_2:list)->list:

    '''
    '''

    maximo = len(lista_1)

    lista_retorno = [False] * maximo
    indice_retorno = 0
    for i in range(maximo):
        bandera = False
        for j in range(len(lista_2)):
            if lista_1[i] == lista_2[j]:
                bandera = True
                break
        
        if bandera == False:
            lista_retorno[indice_retorno] = lista_1[i]
            indice_retorno += 1

    lista_retorno = recortar_lista(lista_retorno)

    return lista_retorno

