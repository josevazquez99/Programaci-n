'''
Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
◦ El exponente sea 0, el resultado es 1.
◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.'''
base = int(input("Introduce la base de la potencia"))
exponente = int(input("Introduce el exponente de la potencia"))
if exponente < 0 :
    resultado = 1/base**abs(exponente)
elif exponente == 0 :
    resultado=1
else :
    resultado = base ** exponente
print(resultado) 