"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 10 Dec 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Crear función que reciba una cadena como parámetro y que devuelva si es una contraseña
FUERTE (True) o DÉBIL (False). Se considera que una contraseña es fuerte si contiene 8 o
más caracteres, y entre ellos al menos hay una mayúscula, una minúscula y un dígito.
 
 """
def mayuscula(cadena):#creamos la funcion mayuscula para ver si en la cadena hay alguna mayuscula
    if ord(cadena)>=65 and ord(cadena)<=90:#hacemos referencia del codigo ascii
        return True
    else:
        return False
def minuscula(cadena):#creamos la funcion minuscula para ver si en la cadena hay alguna minuscula
    if ord(cadena)>=97 and ord(cadena)<=122:#hacemos referencia del codigo ascii
        return True
    else:
        return False
def numero(cadena):#creamos la función numero para comprobar que la cadena incorpora algún numero
    if ord(cadena)>=48 and ord(cadena)<=57:#hacemos referencia del codigo ascii
        return True
    else:
        return False
def contraseña(cadena):#creamos la funcion contraseña 
    for i in range(len(cadena)):#introducimos un contador para comprobar la longitud de la cadena y si incorpora alguna funcion anterior
        if (len(cadena[i]))>=8 and cadena[i]==mayuscula(cadena) and cadena[i]==minuscula(cadena) and cadena[i]==numero(cadena):
            return True
        else:
            return False

print(contraseña("Joselito5"))




    



        
     
     
 