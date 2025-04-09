altura = float(input("¿Cuál es la altura? "))

if altura < 160:
    print("Es base")
elif altura < 180:
    print("Es escolta")
elif altura < 200:    
    print("Es alero")
else:
    print("Es ala-pivot o pivot")