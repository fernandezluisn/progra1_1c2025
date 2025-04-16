def calcular_precio_con_iva(costo: float, 
                            iva: float = 21)-> float:

    '''
    En la documentación voy a explicar qué hace la función,
    qué tipo de valores recibe la función, 
    qué tipo de valores retorna.
    '''

    precio_con_iva = costo * (1 + iva * 0.01)
    return precio_con_iva

#parámetros opcionales
valor_con_iva = calcular_precio_con_iva(20)

print(valor_con_iva)

#parámetros posicionales
valor_con_iva_2 = calcular_precio_con_iva(25, 10.5)

print(valor_con_iva_2)

valor_con_iva_3 = calcular_precio_con_iva(iva = 10.5, costo = 25)
print(valor_con_iva_3)
