from math import sqrt 
x1 = int(input("Dime la coordenada X del primer punto"))
y1 = int(input("Dime la coordenada Y del primer punto"))
x2 = int(input("Dime la coordenada X del segundo punto"))
y2 = int(input("Dime la coordenada Y del segundo punto"))
distancia= sqrt((x1-x2)** 2 +(y1-y2)** 2)
print("la distancia es " + str(distancia))