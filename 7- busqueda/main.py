from paquete.funciones_busqueda import *

# #utilizando búsqueda lineal orden de complejidad 10
# lista_1 = [99, 3, 5, 7, 9, 4, 2, 11, 19, 8]

# #utilizando búsqueda lineal orden de complejidad 4
# lista_2 = [1, 3, 8, 9]


# mensaje = "Ingrese un número positivo para verificar si se encuentra en la lista: "
# numero_buscado = int(input(mensaje))

# while numero_buscado < 0:
#     numero_buscado = int(input(mensaje))

#posicion = buscar_lineal(lista_1, numero_buscado)

# if posicion != None:
#     print(f"El índice es {posicion}")
# else:
#     print("El número no se encuentra en el listado")

lista_ordenada = [1, 3, 8, 9, 11, 12, 13, 15, 16]

# se ejecuta 7 veces
print(buscar_lineal(lista_ordenada, 16))
# se ejecuta 3 veces
print(buscar_binaria(lista_ordenada, 16))
