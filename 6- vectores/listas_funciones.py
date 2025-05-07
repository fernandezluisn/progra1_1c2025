lista = [1, 2]

def mostrar_lista(una_lista: list) -> None:

    if type(una_lista) == list:
        for i in range(len(una_lista)):
            print(una_lista[i])
    else:
        print(f"La variable recibida por parámetro debe ser de tipo lista, no {type(una_lista)}")

mostrar_lista(lista)

mostrar_lista(3)
mostrar_lista(3.14)