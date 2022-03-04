"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 22 Oct 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Design a program that asks for a set of numbers. After inputting each number, the
program should ask “Do you want to enter more numbers (Y/N)?”. If the answer is “Y”
the program asks for other numbers. When the user finishes to enter all the numbers,
the program should say which one is the smallest. The messages are the following:
“Enter one number:”
“Do you want to enter more number (Y/N)?”
“The smallest number is XX”
 
 """
num=int(input("introduce un numero"))
pregunta=input("Quieres introducir mas numeros si o no")
contador=0
while pregunta!="N":
    contador=contador+num
    num=int(input("introduce un numero"))
    pregunta=input("Quieres introducir mas numeros")
    if num<contador:
        num=contador
if pregunta=="N":
    print("el numero mas pequeño es" ,contador)