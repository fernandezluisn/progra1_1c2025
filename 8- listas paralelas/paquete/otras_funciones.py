def recortar_lista(lista: list):

    '''
    '''

    for i in range(len(lista)):
        if lista[i] == False:
            indice_final = i
            break
    
    lista = lista[0: indice_final]

    return lista