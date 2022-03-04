base = int(input("Dime un numero real para la base"))
exponente = int(input("Dime un numero entero positivo para el exponente"))
cont = 1
for i in range(exponente) :
    cont = cont * base
print(cont)