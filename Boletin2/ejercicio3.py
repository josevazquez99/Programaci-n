"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 22 Oct 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Design a program that asks how many numbers the user wants to introduce. Then,
the user would have to introduce the numbers one by one and the program should
say if each one of the numbers is odd or even. If the user inputs 0 or a negative
number, it is not valid, and the system should ask for another number. The messages
are the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The number XX is odd”
“The number XX is even”
 
 """
num=int(input("Cuantos numeros va a introducir"))
contador=0
while num!=0:
    