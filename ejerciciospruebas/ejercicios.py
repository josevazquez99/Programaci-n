"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 2 Dec 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: El índice de masa corporal o IMC es una medida que se utiliza para evaluar el riesgo de enfermedad
cardiovascular. Para su cálculo se divide el peso en kilogramos por la altura en metros elevados al
cuadrado, de forma que un peso normal o normopeso estaría situado en un valor de IMC entre 18,5 y
24,9.
Crea un programa que pida la altura, peso y edad de una persona y calcule e informe del valor y tipo
de IMC obtenido atendiendo al siguiente criterio:
<18,5 Peso insuficiente
18,5-24,9 Normopeso
25-29,9 Sobrepeso
30-39,9 Obesidad
>40 Obesidad mórbida
Además de facilitar el IMD, debe proporcionar un mensaje de recomendación sanitaria si la edad de
la persona es superior a 45 y excede el normopeso (IMC >25), o bien, si ésta tiene obesidad (IMC
>30). Por ejemplo:
Para un peso de 90 kilogramos y una talla de 1.80 metros, su IMC es: 27.78
Usted se encuentra en el grupo: Sobrepeso.
Caso 1 - Dada su edad e IMC es recomendable que cuide su salud cardiovascular
Caso 2 - Dado su IMC es muy recomendable que cuide su salud cardiovascular
Este programa debe validar la información proporcionada y terminar cuando se introduzca un valor
negativo en cualquier medida (edad, peso o tamaño)
 
 """
# altura=float(input("introduce la altura que usted tiene"))
# peso=float(input("introduce lo que usted pesa"))
# edad=int(input("introduce la edad que tienes"))
# iDM=0
# pI=("Peso insuficiente")
# nP=("Normopeso")
# sP=("Sobrepeso")
# o=("Obesidad")
# oM=("Obesidad morbida")
# cASO=0
# cASO1=("Dada su edad e IMC es recomendable que cuide su salud cardiovascular")
# cASO2=("Dado su IMC es muy recomendable que cuide su salud cardiovascular")
# if altura <0 or edad<0 or peso<0:
#    altura=float(input("Vuelve a introducir la altura que usted tiene mayor que 0"))
#    peso=float(input("introduce lo que usted pesa mayor que 0"))
#    edad=int(input("introduce la edad que tienes mayor que 0"))
# else:
#     valor=peso/altura**2
#     if valor<18.5:
#         iDM=pI
#     elif valor>40:
#         iDM=oM
#     elif valor >18.5 and valor <24.9:
#         iDM=nP
#     elif valor >25 and valor<29.9 and edad>25:
#         iDM=sP
#         cASO=cASO1
#     elif valor>30 and valor <39.9:
#         iDM=o
#         cASO=cASO2
#
# print("Usted tiene ", iDM , CASO)
    
"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 2 Dec 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Juan recibe un regalo económico de su familia todos sus cumpleaños, de forma que cada año recibe
15€ más que en el anterior.
Elabora un programa que pida una edad y calcule cuánto dinero en total ha recibido Juan en regalos
de cumpleaños hasta esa edad sabiendo que en el primer cumpleaños le regalaron 20€.
Ejemplo 1: 1 año ⇒ 20€ (recibe el 1º año)
Ejemplo 2: 2 años ⇒ 55€ (= 20€ tenía +35€ recibe el 2º año)
Ejemplo 3: 3 años ⇒ 105€ (= 55€ tenía +50€ recibe el 3º año)
Ampliación: modifica el programa anterior para que tanto la cantidad que se incrementa cada año
como el regalo inicial cambien en cada programa.
 
 """
edad=int(input("Introduce edad"))
dinerobase=20
acumulador=20
for i in range (1,edad):
    acumulador=acumulador+15
    dinerobase=dinerobase+acumulador
print("El total que ha recibido es ", dinerobase)


"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 2 Dec 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Un juguete tiene tres botones, dos de melodías: A y B (con dos músicas por botón) y otro P de
apagado. Cada botón de melodía activa el juguete y al ser pulsado sucesivamente cambia de una a
otra melodía.
Es decir, si se pulsa el botón A una vez suena la melodía A1 y si se vuelve a pulsar, la A2, y de igual
modo sucede con el botón B.
Crea un programa que lea por teclado el botón que se ha pulsado (independientemente de si es
mayúscula o minúscula) y escriba la melodía que suena (melodía A1, … melodía B2) y se apague
cuando se pulse el botón P
 
 """
 
#

        
        
        
        
        
        
        
        
        
        
        
        
        
        
   
 
