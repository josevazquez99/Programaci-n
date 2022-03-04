"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 29 Oct 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Vamos a escribir un programa para codificar una clave que el usuario deberá introducir por
teclado, así, cuando sepamos escribir en ficheros, en vez de guardar la clave guardaremos la
codificación, aunque por ahora lo que haremos es escribirla por pantalla.
La generación de la clave se hará en función de la seguridad que quiera el usuario por lo que lo
primero que debemos hacer es pedirle cuántos números quiere introducir para generar la clave. A
continuación se le deberán preguntar los números y la clave se generará sumando el resto de dividir
los números entre 5, siempre y cuando los números sean impares. Aunque se introduzcan números
negativos se debe sumar el resto nunca restar.
Es decir, el programa debe preguntar ¿cuántos números quieres para la clave? Si le digo por
ejemplo 6, debe preguntarme los seis números, si mi respuesta es:
235 → El resto es 0, no tengo que hacer nada
458 → El resto es 3 es impar lo sumo
6 → El resto es 1, es impar lo sum
-679 → El resto es -4, es par, no lo sumo
89 → El resto es 4, es par, no lo sumo
-88 → El resto es 3, es impar, lo sumo
El resultado de la clave es 7
 
 """
cantidad=int(input("cuantos numeros quieres para la clave"))#creamos la variable cantidad
contador=0#creamos un contador
for i in range(0,cantidad):#creamos el bucle para calcular el resto y si es par o impar
    num=abs(int(input("dime un numero")))
    resto=num%5
    if resto%2 !=0:
        contador=contador+resto
    else:
        contador==contador
print("el resultado es" + str(contador))#imprimos el resultado
        