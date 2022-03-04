num=int(input("introduce un numero"))
contador=0
acumulador=0
maximo=num
minimo=num
while num!=0:
    if num<minimo:
        minimo=num
    elif num>maximo:
        maximo==num
    contador=contador+1
    acumulador=acumulador+num
    num=int(input("introduce un numero"))
media=acumulador/contador
print("la media es" + str(media))
print("el maximo es " + str(maximo))
print("el minimo es " + str(minimo))