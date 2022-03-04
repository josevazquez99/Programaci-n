#Decir un numero del 1 al 12 y decir el mes
num=int(input("Dime un numero"))
for num in (2,12):
    print("31 dias")
for num in [4,6,9,11]:
    print("30 dias")
if num> 12:
    print("mes incorrecto")