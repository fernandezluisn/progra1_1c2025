# buscamos valor mínimo gastado en el día
bandera = True
acumulador = 0

while acumulador < 20000:

    valor = float(input("Ingrese el valor del gasto realizado: "))

    if bandera == True:
        gasto_minimo = valor
        bandera = False
    elif valor < gasto_minimo:
        gasto_minimo = valor

    #if valor > gasto_maximo:
    #    gasto_maximo = valor

    acumulador += valor

    print(f"Lleva gastados ${acumulador}")
    print(f"El gasto mínimo fue ${gasto_minimo}")