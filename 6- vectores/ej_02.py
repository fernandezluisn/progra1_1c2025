# definición de listas
lista_nueva = list()
lista_nueva_2 = []

vector_numeros = [1, 3, 4, 5]

acumulador = 0

#observamos utilidad de función
print(f"La cantidad de elementos del vector es {len(vector_numeros)}")

cantidad_de_elementos = len(vector_numeros)

for i in range(cantidad_de_elementos):
    print(f"indice = {i}")
    print(f"valor = {vector_numeros[i]}")

    acumulador += vector_numeros[i] 

promedio = acumulador / len(vector_numeros)

print(f"promedio= {promedio}")