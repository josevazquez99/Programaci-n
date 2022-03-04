euros2 = int(input("Introduce cuantas monedas de 2e tienes"))
euros1 = int(input("Introduce cuantas monedas de 1e tienes"))
cent50 = int(input("Introduce cuantas monedas de 50cent tienes"))
cent20 = int(input("Introduce cuantas monedas de 20cent tienes"))
cent10 = int(input("Introduce cuantas monedas de 10cent tienes"))
dinero = 0
if euros2 > 0 :
    dinero = dinero + euros2 * 2
if euros1 > 0 :
    dinero = dinero + euros1 * 1
if cent50 > 0 :
    dinero = dinero + cent50 * 0.5
if cent20 > 0 :
    dinero = dinero + cent20 * 0.2
if cent10 > 0 :
    dinero = dinero + cent10 * 0.1
print("Tienes " + str(dinero) + " euros")