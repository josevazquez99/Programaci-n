mes = input("Dime un numero del 1 al 12 y te dire cuantos dias tiene ese mes")
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 :
    print("31 dias")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 :
    print("30 dias")
else :
    print("28 dias/ 29 dias si es bisiesto el anno")