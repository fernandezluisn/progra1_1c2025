contador = 0

while contador < 5:

    contador += 1
    print(contador)

    seguir = input("¿Quiere seguir montrando numeros? s/n: ")

    if seguir == "n":
        break

