base = int(input("Introduce la base de la potencia"))
exponente = int(input("Introduce el exponente de la potencia"))
potencia =1
if exponente == 0:
    print("La el resultado de la potencia es => 1")
elif exponente <0:
    exponente *=-1 
    for i in range (exponente):
        potencia *=base
        resul = 1/potencia
    print("La el resultado de la potencia es => 1/" +str(potencia)+"=> "+str(resul))
else:
    for i in range (exponente):
        potencia *=base
    print("La el resultado de la potencia es => 1/" +str(potencia)+"=> "+str(resul))