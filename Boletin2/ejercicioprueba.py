"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 25 Oct 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Realizar un programa que solicite números enteros al usuario. El programa
debe terminar cuando el usuario introduzca -1. Al final del programa se nos 
informará de la suma de todos los números introducidos por el usuario (menos el
-1 que nos servirá para salir) y de si hay algún número par o no entre 
los introducidos por el usuario.
 
 """
num=int(input("Dime numeros"))
acumulador=0
par=True
while num!=-1:
    if num%2==0:
        par=False
    acumulador+=num
    num=int(input("Dime un numero"))
    
if par==True:
    print("la suma de sus numeros es " + "=" + str(acumulador) + " y hay numeros impares")
else:
    print("la suma de sus nuemros es" + "=" + str(acumulador) + "y hay numeros pares")