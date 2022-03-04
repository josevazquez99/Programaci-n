import math
a = int(input("Introduce cuanto mide el lado del triangulo"))
b = int(input("Introduce cuanto mide el otro lado del triangulo"))
c = int(input("Introduce cuanto mide el ultimo lado del triangulo"))
if c == math.sqrt(a**2 + b**2) :
    print("El triangulo es rectangulo")
elif a == b or a == c or b == c :
    print("El triangulo es isósceles")
elif a == b and a == c and b == c :
    print("El triangulo es equilatero")
else :
    print("El triangulo es escaleno")