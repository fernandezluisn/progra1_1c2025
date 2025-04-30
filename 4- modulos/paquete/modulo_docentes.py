from .modulo_alumnos import saludo_alumno

saludo_docente = "Hola profesor"

def calcular_salario(horas_dictadas: int, 
                     valor_hora: float)-> float:
    
    '''
    '''

    salario_final = horas_dictadas * valor_hora

    print(f"El salario final {salario_final}")

    #return salario_final

