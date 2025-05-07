lista_numeros = [10, 33, 5, 13, 14]

# puedo acceder a variables dentro de la lista
print(lista_numeros[1])
print(f"ID: {id(lista_numeros)}")

lista_numeros[1] = 9

print(lista_numeros[1])
print(f"ID: {id(lista_numeros)}")

print(lista_numeros[-1])

for i in range(len(lista_numeros) - 1, -1, -1):
    print(f"El elemento en el indice {i} es {lista_numeros[i]}")

lista_numeros[1] = "Pedro"

for i in range(len(lista_numeros) - 1, -1, -1):
    print(f"El elemento en el indice {i} es {lista_numeros[i]}")
