def mostrar_matriz(matriz: list)-> None:

    '''
    Recibe una matriz y la muestra por consola.
    No retorna nada.
    '''

    if type(matriz) != list:
        print("La función debe recibir por parámetro una lista.")
        return None

    for i in range(len(matriz)):

        for j in range(len(matriz[i])):

            valor = matriz[i][j]
            print(valor, end = " ")
        
        print("")

def inicializar_matriz(cant_filas: int = 5,
                       cant_columnas: int = 5,
                       valor_por_defecto: any = 0)-> list:
    
    '''
    '''

    matriz = []

    for _ in range(cant_filas):

        fila = [valor_por_defecto] * cant_columnas

        matriz += [fila]

    return matriz

def cargar_matriz_secuencial(matriz: list)->list:

    for i in range(len(matriz)):
        for j in range (len(matriz[i])):

            matriz[i][j] = int(input(f"Ingrese un número en fila {i} columna {j} "))

    return matriz

def cargar_matriz_distribuida(matriz: list)-> list:

    '''
    '''

    seguir = "S"

    while seguir == "S":
        fila = int(input("Ingrese la fila en la que desea ingresar valor "))
        columna = int(input("Ingrese la columna en la que desea ingresar valor "))
        valor = int(input("Ingrese el nuevo valor "))
        matriz[fila][columna] = valor
        seguir = input("¿Desea continuar con la carga de valores? S/N ")

    return matriz

def buscar_matriz(matriz: list,
                  numero: int)-> int:
    
    '''
    '''

    print("Se ejecuta función de búsqueda")

    for i in range(len(matriz)):
        
        for j in range(len(matriz[i])):

            print(matriz[i][j])

            if matriz[i][j] == numero:
                print(f"El {numero} se encuentra en fila {i} columna {j}") 
                return i
            
def sumar_matrices(matriz_1: list,
                   matriz_2: list)-> list:
    
    '''
    '''

    if type(matriz_1) != list or type(matriz_2) != list:
        print("los parámetros deben ser de tipo lista.")
        return None
    
    if (len(matriz_1) != len(matriz_2) or 
        len(matriz_1[0]) != len(matriz_2[0])):
        print("las matrices deben ser del mismo tamaño.")
        return None


    matriz_resultado = inicializar_matriz(len(matriz_1), len(matriz_1[0]))

    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            matriz_resultado[i][j] = matriz_1[i][j] + matriz_2[i][j]

    return matriz_resultado