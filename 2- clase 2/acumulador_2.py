gastos_diarios = 0
cantidad_gastos = 0
limite = 20000
maximo = 25000

while gastos_diarios < limite:
    valor = float(input("ingrese el costo del gasto realizado: "))

    if gastos_diarios + valor > maximo:
        print("Ese gasto supera el monto permitido")
    else:
        gastos_diarios += valor
        cantidad_gastos += 1
        porcentaje_gastado = (gastos_diarios * 100) / limite
        promedio_gastos_diarios = porcentaje_gastado / cantidad_gastos
        print(f"Lleva gastados ${gastos_diarios}")
        print(f"Cada gasto implicó un {promedio_gastos_diarios}%")

        print(f"Lleva gastados {porcentaje_gastado}%")

    if gastos_diarios >= limite: 
        print("Se han excedido los gastos diarios")