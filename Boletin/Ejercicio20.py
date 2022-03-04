dinero = int(10)
cont = int(1)
for cont in range (1,20) :
    print(str(cont) + " " + str(dinero))
    dinero = dinero * 2
    cont=cont + dinero
print("20 " + str(dinero))
print("el dinero total es"+ str(cont))