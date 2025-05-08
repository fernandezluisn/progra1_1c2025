from paquete.matrices import *

# matriz = [[2, 4, 5, 8], 
#           [6, 3, 1, 9]]

# tabla_estudiantes = [["Juan", "Perez", 23, 8],
#                      ["Juana", "Díaz", 20, 7]]

# print(matriz)
# mostrar_matriz(matriz)


# print(tabla_estudiantes)
# mostrar_matriz(tabla_estudiantes)

# #modificamos el 8 de la matriz de arriba
# matriz [0][3] = 19

# mostrar_matriz(matriz)

# matriz_2 = inicializar_matriz()
# mostrar_matriz(matriz_2)

# matriz_3 = inicializar_matriz(3, 4, "a")
# mostrar_matriz(matriz_3)

matriz_sin_cargar = inicializar_matriz(3, 2)

matriz_cargada = cargar_matriz_secuencial(matriz_sin_cargar)

print("Cargamos matriz con carga secuencial")

mostrar_matriz(matriz_cargada)

print("Modificamos matriz con carga aleatoria")

matriz_modificada = cargar_matriz_distribuida(matriz_cargada)

mostrar_matriz(matriz_modificada)

retorno_busqueda = buscar_matriz(matriz_cargada, 33)

# if retorno_busqueda == None:
#     print("No se encontró el valor buscado")
# else:
#     print(f"Se encontró el número en la fila {retorno_busqueda}")

# print(id(retorno_busqueda))
# print(retorno_busqueda)
# print(type(retorno_busqueda))

matriz_4 = [[1,2],
            [3,4],
            [5,6]]

mostrar_matriz(sumar_matrices(matriz_4, matriz_modificada))