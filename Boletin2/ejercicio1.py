"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 22 Oct 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Design a program to show all numbers between 1 and 100. If the number is a
multiple of 7 you should show the message "The number xx is a multiple of 7". If the
number is a multiple of 13 you should show the message "The number xx is a
multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages.
 
 """
cuenta=0
for num in range(101):
    if num % 7 == 0:
        cuenta=cuenta+1
        print("el numero" + str(cuenta) + "es multiplo de 7")
    elif num % 13 == 0:
        cuenta=cuenta+1
        print("el numero" + str(cuenta) + "es multiplo de 13")
    elif num % 7 == 0 and num % 13 == 0:
        cuenta=cuenta+1
        print("el numero" + str(cuenta) + "es multiplo de 7 y 13") 