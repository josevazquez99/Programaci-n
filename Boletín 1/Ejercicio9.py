base = int(input("Introduce la base de la potencia"))
exponente = int(input("Introduce el exponente de la potencia"))
potencia = base ** exponente
if exponente < 0 :
    exponente = abs(exponente)
    resultado = 1 / potencia
    print(resultado)
elif exponente == 0 :
    print(1)
else :
    print(potencia)