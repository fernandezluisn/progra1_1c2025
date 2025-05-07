lista_1 = [1]

#copiando el id
lista_2 = lista_1

print(f"lista 2: {lista_2}")

lista_1[0] = 5

print(f"lista 2: {lista_2}")

print(id(lista_1))
print(id(lista_2))