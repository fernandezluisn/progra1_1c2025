class Calculadora:

    def __init__(self):
        self.resultado = 0

    def dividir(self, dividendo, divisor):
        if dividendo != 0 and divisor != 0:
            self.resultado = dividendo / divisor
            print(f"El resultado es {self.resultado}")
        else:
            print("El dividendo y el divisor deben ser distintos de 0")

obj_calculadora = Calculadora()

obj_calculadora.dividir(4, 2)