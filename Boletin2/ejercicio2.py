"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 22 Oct 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Design a program for reading an integer between 0 and 10 and show the times table.
To ask for the number you should show the next message "Enter one number
between 0 and 10”. If the number is out of the boundaries, the program should show
the message “The number is out of the boundaries”. If the number is valid, it should
show the times table following the next format:
7*0=0
7*1=7
…..
7*10=70
 
 """
num=int(input("introduce un numero entre 0 y 10"))
if num<0 or num>10:
    print("el numero esta fuera de los limites")
num=int(input("introduce otro numero"))
suma=num
for num in range(0,11):
    print("el numero" + str(suma) + "*" + str(num) + "=" + str(suma*num) )