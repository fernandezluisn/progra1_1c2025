from paquete.validacion import validar_numero

cadena_de_caracteres = "123 wqz"

for i in range(len(cadena_de_caracteres)):

    if cadena_de_caracteres[i] != " ":

        print(cadena_de_caracteres[i])

cadena_comillas = "123 \"cadena\""

print(f"ejemplo slicing: {cadena_comillas[4:]}")

#concatenación de cadenas

cadena_concatenada = cadena_de_caracteres + " separo " + cadena_comillas

print(f"cadena concatenada: {cadena_concatenada}")
print(f"cadena repetida: {cadena_de_caracteres * 3}")
print(cadena_de_caracteres > cadena_comillas)

print(f"indexación {cadena_de_caracteres[1]}")

#cadena_de_caracteres[1] = "3"

cadena_concatenada += " agregando caracteres al final de la cadena"

print(f"cadena concatenada: {cadena_concatenada}")

#valores ascii

print(f"a: {ord("a")}")
print(f"A: {ord("A")}")
print(f"espacio: {ord(" ")}")

print("a" > "A")

continuar = "s"

while continuar == "s":

    valor = input("Ingrese un caracter y responderemos si es un número: ")

    if validar_numero(valor):
        valor_entero = int(valor)
        print(f"{valor} es un número")
    else:
        print(f"{valor} no es un número")

    continuar = input("¿Desea continuar? s/n: ")



