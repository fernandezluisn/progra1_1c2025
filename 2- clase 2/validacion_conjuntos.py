color = input("Ingrese un color primario: ")

while color != "rojo" and color != "amarillo" and color != "azul":
    color = input("Error. Ingrese un color primario: ")

print(f"El color primario ingresado es: {color}")