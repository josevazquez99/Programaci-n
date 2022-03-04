"""
# coding: utf-8
 @autor: Jose Antonio Vázquez Fernández
 @fecha: 10 Dec 2021
 @nombre: Boletin  - Ejercicio  
 @enunciado: Un oficial de correos decide optimizar el trabajo de su oficina cortando todas las palabras de
más de cinco letras a sólo cinco letras (e indicando que una palabra fue cortada con el
agregado de una arroba). Además también elimina todos los espacios en blanco de más.
Por ejemplo, al texto » Llego mañana alrededor del mediodía » se transcribe como «Llego
mañan@ alred@ del medio@».
Por otro lado cobra un valor para las palabras cortas y otro valor para las palabras largas
(que deben ser cortadas).
Escribir una función que reciba un texto, la longitud máxima de las palabras (en el caso
anterior eran 5 letras) y devuelva como resultado el texto del telegrama.
 
 """
def espacio(cadena):#creamos la funcion quitar espacios en blanco
    frase=[]
    cadenanueva=' '
    for i in range(len(cadena)):#un contador para la longitud de la cadena para quitar espacios
        if cadena[i]!=' ':
            cadenanueva+=cadena[i]
            frase.append(cadenanueva)
    return cadenanueva
     

print(espacio("jose tiene  hambre"))

def contarletras(cadena):
    contador=0
    for i in range(cadena):
        contador+1
    return contador
        

def cortapalabras(cadena):
    palabracambiada="@"
    
    
    
    


        
    
    
    
    
    