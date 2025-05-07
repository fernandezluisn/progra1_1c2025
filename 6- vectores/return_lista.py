def inicializar_lista(tamanio: int)->list:

    if type(tamanio) == int:
        lista_ceros = [0] * tamanio

        #carga secuencial
        for i in range(len(lista_ceros)):
            valor_nuevo = int(input(f"Ingrese el valor para el indice {i} "))

            lista_ceros[i] = valor_nuevo

        return(lista_ceros)
    else:
        print("Tamaño debe ser entero")

lista_nueva = inicializar_lista(3)

print(lista_nueva)

    