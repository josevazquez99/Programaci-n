edad=int(input("cual es tu edad"))#creamos la variable edad
covid=input("has pasado el covid")#creamos la variable covid para saber si ha pasado o noel covid
covidsi="si"
covidno="no"
vacuna=input("Cual de las vacunas has recibido , Pfizer, Moderna o Astrazeneca")
Phizer="phizer"
Moderna="moderna"
Astrazeneca="astrazeneca"
while vacuna!=Astrazeneca and vacuna!=Phizer and vacuna!=Moderna or edad<0:#creamos el bucle para volver a preguntar si los datos no son correctos
    print("has dado unos datos incorrectos")
    edad=int(input("cual es tu edad"))
    covid=input("has pasado el covid")
    vacuna=input("Cual de las vacunas has recibido , Pfizer, Moderna o Astrazeneca")
if vacuna==Astrazeneca:#creamos la condicion si se trata de Astrazeneca
    print("debes volver a vacunarte")
elif vacuna==Moderna and edad>60 and covid==covidno:#creamos la condicion de si se trata de moderna , la edad y que no haya pasado el covid
    print("debes volver a vacunarte")
elif vacuna==Moderna and edad<60:#creamos la condicion de si se trata de moderna y la edad
    print("no debes volver a vacunarte")
elif vacuna==Phizer and covid==covidno:#creamos la condicion de si se trata de la phizer y que no haya pasado covid
    print("debes volver a vacunarte")
elif vacuna==Phizer and covid==covidsi and edad>70:#creamos la condicion de si se trata de phizer , edad y que haya pasado covid
    print("debes volver a vacunarte")
