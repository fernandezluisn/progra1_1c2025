estacion = input("¿Cuál es la estación del año? ")

match estacion:
    case "invierno":
        print("Viaja a Bariloche")
    case "verano":
        print("Viaja a Mar Del Plata y Cataratas")
    case "otoño":
        print("Viaja a todos los lugares")
    case "primavera":
        print("Viaja a todos los lugares menos Bariloche")
