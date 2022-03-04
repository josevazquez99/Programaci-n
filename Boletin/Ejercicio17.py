num1=int(input("Introduce un numero"))
num2=int(input("Introduce otro numero"))
if num1<num2:
    minimo=num1
    maximo=num2
else:
    minimo=num2
    maximo=num1
for i in range(minimo,maximo):
    if i%2==0:
        print(i)