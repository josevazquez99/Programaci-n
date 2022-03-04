precioinicial =int(input("Introduce el precio inicial"))
kilos=int(input("Introduce los kilos que quieras"))
tipo=input("Que tipo es (A/B)")
tamano = int(input("De que tamano quieres (1/2)"))
if tipo == "A" :
    if tamano == 1 :
        precio = precioinicial + 0.2
        ganacia= kilos *0.2
        print(precio)
    elif tamano == 2 :
        precio = precioinicial + 0.3
        ganacia=kilos*0.3
        print(precio)
elif tipo == "B" :
    if tamano == 1 :
        precio = precioinicial - 0.3
        ganancia=kilos*-0.3
        print(precio)
    elif tamano == 2 :
        precio = precioinicial - 0.5
        ganancia=kilos*-0.5
        print(precio)