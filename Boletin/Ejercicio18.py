inferior=int(input("Dame un limite"))
superior=int(input("Dame otro limite"))
while inferior>=superior:
    inferior=int(input("Introduce numero valido"))
suma=0
estanfuera=0
intervalo="no"
num=1
while num!=0:
    num=int(input("Introduce un numero"))
    if num>inferior or num<superior:
        suma=suma +num
    elif num<inferior or num>superior:
        estanfuera+=1
    else:
        intervalo="si"  
       
print("la suma es"+str(suma))        
print(("hay "+str(estanfuera)+"fuera de rango")) 
if intervalo=="si":
    print("Se introducio un numero limite") 