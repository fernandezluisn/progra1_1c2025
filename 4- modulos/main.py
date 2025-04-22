#import modulos.modulo_alumnos

#promedio = modulos.modulo_alumnos.calcular_promedio(90, 10)

#print(modulos.modulo_alumnos.saludo_alumno)
#print(f"Su promedio es {promedio}")

from modulos.modulo_alumnos import saludo_alumno, calcular_promedio

promedio = calcular_promedio(90, 10)

print(saludo_alumno)
print(f"Su promedio es {promedio}")