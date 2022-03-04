"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 22 Oct 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Design a program that asks how many numbers the user wants to write. After the
user enters all numbers, the program should say the medium of the numbers. If the
user inputs a wrong number, the program should ask for it again. The messages are
the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The medium is XX.XX” to show the result
 
 """

num=int(input("cuantos numeros quieres introducir"))
acumulador=0
contador=0
while contador<num:
    cantidad=int(input("introduce numeros"))
    acumulador+=cantidad
    contador+=1
    if cantidad<=0:
        print("el numero no es valido, deberia ser mayor que 0")
print("la media es",acumulador/num)