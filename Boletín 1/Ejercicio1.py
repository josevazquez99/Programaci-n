import math
cat1 = int(input("Introduce un valor"))
cat2 = int(input("Introduce otro valor"))
if cat1<0 or cat2<0:
    print("Los catetos deben ser positivos")
else:
    hipotenusa = math.sqrt(cat1**2 + cat2**2)
    print(hipotenusa)