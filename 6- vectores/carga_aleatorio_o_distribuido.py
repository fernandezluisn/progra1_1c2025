lista_nueva = [0] * 5

print(lista_nueva)

cargar = "s"

while cargar == "s":

    i = int(input("ingrese posición de la lista que desea modificar "))

    if i < len(lista_nueva) and i >= 0:
        lista_nueva[i] = int(input("ingrese valor que desea ingresar "))
    else:
        print("Indice incorrecto")

    cargar = input("¿Quiere cargar otro elemento? s/n ")

for i in range(len(lista_nueva)):    

    print(lista_nueva[i]) 