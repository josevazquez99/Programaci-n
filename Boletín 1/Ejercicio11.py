anno = int(input("Introduce un anno"))
if anno % 4 == 0 and anno % 100 != 0 or anno % 400 == 0 :
    print("Es un anno bisiesto")
else :
    print("No es bisiesto")