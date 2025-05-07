lista_ceros = [0] * 10

#carga secuencial
for i in range(len(lista_ceros)):
    valor_nuevo = int(input(f"Ingrese el valor para el indice {i} "))

    lista_ceros[i] = valor_nuevo

#visualización
for i in range(len(lista_ceros)):    

    print(lista_ceros[i]) 

