# Este contador cuenta la cantidad de vocales ingresadas
contador_vocales = 0

while contador_vocales < 10:

    letra = input("Ingrese una letra: ")

    if letra == "a":
        contador_vocales += 1
    elif letra == "e":
        contador_vocales += 1
    elif letra == "i":
        contador_vocales += 1
    elif letra == "o":
        contador_vocales += 1
    elif letra == "u":
        contador_vocales += 1
    
    print(f"Se ingresaron {contador_vocales} vocales")

