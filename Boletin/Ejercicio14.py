tiempo=int(input("Dame el tiempo de la llamda en minutos: "))
dia=input("Introduce el día de la semana: ")
if dia!="Domingo" and dia!="domingo":
    momento=input("¿La llamada se realizó en la mañana o en la tarde? ")
precio=0
if tiempo>10:
    tiempo-=10
    precio=tiempo*0.50+8.8
elif tiempo>=8:
    tiempo-=8
    precio=tiempo*0.70+7.4
elif tiempo>=5:
    tiempo-=5
    precio=tiempo*0.80+5
else:
    precio+=tiempo*1

if dia=="Domingo" or dia=="domingo":
    porcentaje=precio*10/100
    precio+=porcentaje
elif momento=="Mañana" or momento=="mañana":
    porcentaje=precio*15/100
    precio+=porcentaje
else:
    porcentaje=precio*10/100
    precio+=porcentaje
print("El precio que pagará por la mañana será de {precio} euros")