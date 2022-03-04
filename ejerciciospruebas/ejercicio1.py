num=int(input("introduce un numero"))
contador=0
if num<=0:
    print("el numero no es valido intentalo de nuevo")
    num=int(input("introduce un numero"))
for i in range(1,num):
    if num%i==0:
        contador += i
if num == contador :      
    print("es perfecto")
else:
    print("el numero no es perfecto")
