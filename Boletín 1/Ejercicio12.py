kilo = int(input("Cuantos kilos quieres"))
tipo = input("Que tipo es (A/B)")
tamano = int(input("De que tamano quieres (1/2)"))
precio = int(15)
if tipo == "A" :
    if tamano == 1 :
        precio = precio + 0.2
        print(precio)
    elif tamano == 2 :
        precio = precio + 0.3
        print(precio)
elif tipo == "B" :
    if tamano == 1 :
        precio = precio - 0.3
        print(precio)
    elif tamano == 2 :
        precio = precio - 0.5
        print(precio)