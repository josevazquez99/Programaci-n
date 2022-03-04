"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 22 Oct 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado:  Design a program that reads two integer numbers, for example numberA and
numberB, and calculates the product of both numbers without use multiplication, but
using the sum. The messages are the following:
“Enter one number:”
“The product is XX”
 
 """
num1 = int(input("Dime un numero"))
num2 = int(input("Dime otro numero"))
cont = 0
for i in range(num2):
    cont = cont + num1
print("el producto es" + str(cont))