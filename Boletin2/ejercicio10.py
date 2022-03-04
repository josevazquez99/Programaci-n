num=int(input("introduce un numero entero positivo"))
contador=0
while num>0:
    if num==0:
        print("el factorial es" + str(1))
    elif num==1:
        print("el factorial es" + str(1))
    elif num>1:
        contador=contador+1
        factorial=num*(num-contador)
        print("el factorial es" + str(factorial))
if num<=0:
    print("el numero no es valido")