def ordenar_por_burbujeo(lista:list)-> list:

    '''
    Recorre una lista y ordena elementos adyacentes.
    Recibe una lista.
    Retorna una lista.
    '''
    if type(lista) != list:
        print("El parámetro que recibe la función debe ser una lista")
        return
    
    n = len(lista)

    for i in range(n):

        print(f"iteración {i}")

        intercambio = False

        for j in range(0, n - i - 1):

            if lista [j] > lista[j + 1]:
                intercambio = True
                menor = lista[j + 1]

                lista[j + 1] = lista[j]
                lista[j] = menor

                print(f"Se intercambió {menor} por {lista[j + 1]}")

        if intercambio == False:
            break

    return lista
