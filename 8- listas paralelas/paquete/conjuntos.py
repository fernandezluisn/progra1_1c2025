def devolver_interseccion(lista_1:list, lista_2:list)->list:

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

    for i in range(maximo):
        if lista_retorno[i] == False:
            indice_final = i
            break
    
    lista_retorno = lista_retorno[0: indice_final]

    return lista_retorno

