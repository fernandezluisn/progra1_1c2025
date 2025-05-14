def ordenar_x_seleccion(lista:list)-> list:

    '''
    Ubica iterativamente el menor valor de la lista en el índice más bajo.
    Recibe un listado.
    Retorna un listado.
    '''

    if type(lista) != list:
        print("El parámetro que recibe la función debe ser una lista")
        return
    
    
    for i in range(len(lista) - 1):

        indice_menor = i

        print(f"iteración {i}")
        for j in range(i + 1, len(lista)):

            if lista[j] < lista[indice_menor]:
                indice_menor = j

        if indice_menor != i:
            menor = lista[indice_menor]
            lista[indice_menor] = lista[i]
            lista[i] = menor
            print(f"intercambio posición {i} por posición {indice_menor}")

        print(lista)
    
    return lista