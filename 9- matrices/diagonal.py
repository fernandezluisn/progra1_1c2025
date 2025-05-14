from paquete.matrices import *

matriz = inicializar_matriz()

mostrar_matriz(matriz)

#deberíamos validar que la matriz es cuadrada

for i in range(len(matriz)):
    matriz[i][i] = 1

print("Matriz modificada")
mostrar_matriz(matriz)
