#import modulos.modulo_alumnos

#promedio = modulos.modulo_alumnos.calcular_promedio(90, 10)

#print(modulos.modulo_alumnos.saludo_alumno)
#print(f"Su promedio es {promedio}")

#from paquete.modulo_alumnos import saludo_alumno, calcular_promedio
#from paquete.modulo_docentes import calcular_salario

from paquete import *

promedio = calcular_promedio(90, 10)

print(saludo_alumno)
print(f"Su promedio es {promedio}")

salario_final = calcular_salario(12, 10)

print(f"El salario final es {salario_final}")