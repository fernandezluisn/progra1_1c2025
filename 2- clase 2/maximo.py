# buscamos valor maximo gastado en el día

bandera = True
acumulador = 0
gasto_maximo = 0

while acumulador < 20000:

    valor = float(input("Ingrese el valor del gasto realizado: "))

    if bandera == True:
        gasto_maximo = valor
        bandera = False
    elif valor > gasto_maximo:
        gasto_maximo = valor

    #if valor > gasto_maximo:
    #    gasto_maximo = valor

    acumulador += valor

    print(f"Lleva gastados ${acumulador}")
    print(f"El gasto máximo fue ${gasto_maximo}")

