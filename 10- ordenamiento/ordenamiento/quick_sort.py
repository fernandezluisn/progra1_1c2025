def ordenar_rapido(lista: list)->list:

    '''
    Ordena los elementos mediante "divide y vencerás" usando un pivote.
    Recibe una lista.
    retorna una lista.
    '''

    if type(lista) != list:
        print("El parámetro que recibe la función debe ser una lista")
        return
    
    menores = []
    iguales = []
    mayores = []

    if len(lista) > 1:
        
        pivote = lista[0]

        for i in range(len(lista)):

            
            if lista[i] < pivote:
                menores += [lista[i]]

            elif lista[i] == pivote:
                iguales += [lista[i]]
            else:
                mayores += [lista[i]]
        
        return ordenar_rapido(menores) + iguales + ordenar_rapido(mayores)

    else:
        return lista
