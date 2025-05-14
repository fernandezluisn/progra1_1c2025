from ordenamiento.burbujeo import *
from ordenamiento.seleccion import ordenar_x_seleccion
from ordenamiento.quick_sort import ordenar_rapido
from ordenamiento.insercion import ordenar_x_insercion

lista_numeros = [6, 3, 44, 1, 7, 9, 8, 12]

# lista_ordenada = ordenar_por_burbujeo(lista_numeros)

# print(lista_ordenada)

lista_ordenada = ordenar_x_insercion(lista_numeros)

print(lista_ordenada)

