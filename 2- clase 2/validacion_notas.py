nota = int(input("Ingrese la nota del examen: "))

while nota < 1 or nota > 10:
    nota = int(input("Error. Ingrese la nota del examen nuevamente: "))

print(f"La nota es {nota}")