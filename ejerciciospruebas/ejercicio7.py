#Design a function called charactersInString that has a character string and a character as
#input parameters and returns how many times that character appears in the string. It should
#do if the string and character are lower case or upper case characters.
from pickle import TRUE, FALSE
def minusculas(caracter):
    if ord(caracter)>=97 and ord(caracter) <= 122:
        return True 
    else:
        return False


def charactersInString (cadena,caracter):
    numApariciones=0
    if minusculas(caracter):
        suma = -32
    else:
        suma = 32
    for i in range(len(cadena)):
        if ord(cadena[i])== ord (caracter) or ord(cadena[i]) == ord(caracter)+suma :
            numApariciones+=1
    return numApariciones


#Design a function called lowCaseInString that has a string of characters as parameter, the
#method should return how many of those characters are lowcase letters.

def lowCaseInString(cadena):
    numApariciones=0
    for i in range(len(cadena)):
        if minusculas(cadena[i])==True:
            numApariciones+=1
    return numApariciones


#Design a function called upperCaseInString that has a string of characters as parameter, the
#method should return how many of those characters are upper case letters
def upperCaseInString(cadena):
    numApariciones=0
    for i in range(len(cadena)):
        if minusculas(cadena[i])== False:
            numApariciones+=1
    return numApariciones 




#Diseña una funcion llamada paseminuscula que me covierta una cadena a minuscula

def mayuscula(cadena):
    resultado=''
    for i in range (len (cadena)):
        if ord(cadena[i])>=65 and ord(cadena[i])<=90:
            resultado=resultado+(cadena[i])
        elif ord(cadena[i])>=97 and ord(cadena[i])<=122:
            suma=ord(cadena[i])-32
            resultado=resultado+(chr(suma))
        else:
            resultado=resultado+cadena[i]
    return resultado
        


#Design a function called numberInString that has a string of characters as parameter, the
#method should return how many of those characters are numbers.

def numberInString(cadena):
    contador=0
    numeros=["1","2","3","4","5","6","7","8","9"]
    for i in range(len(cadena)):
        if cadena[i] in numeros:
            contador+=1
    return contador

print(numberInString("Jose56"))

#Design a function called palindrome that has a string of characters as parameter, and return
#true if it is a palindrome or false in other case. A word is a palindrome, if it is reads the
#same from left to right as from right to left, ignoring whites,. For example: "anilina" or "el
#abad le dio arroz al zorro" To simplify the problem, you can assume that simple characters
#are used, that is, without tildes or diresis

def quitarespacio(cadena):
    resultado=""
    for i in cadena:
        if i !="":
            resultado+=i
    return resultado 

def darVuelta2(cadena):
    resultado=""
    contador= len(cadena)-1
    while contador >=0:
        resultado=resultado+cadena(contador)
        contador-=1
    return resultado
def palindromo(cadena):
    nuevacadena=darVuelta2(mayuscula(quitarespacio(cadena)))
    if mayuscula(quitarespacio(cadena)) == nuevacadena:
        return True
    else:
        return False
    
def palindromo2(cadena):
    return mayuscula(quitarespacio(cadena))==darVuelta2(mayuscula(quitarespacio(cadena)))





#Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si
#la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
#encontrará y deberá devolver True, en caso contrario deberá devolver False.
def buscaryquitarletra(cadena,i):
    i=minusculas(i)
    cadena=minusculas(cadena)
    heencontradolaprimeraletra= False
    nueva=""
    for j in cadena:
        if j==i and heencontradolaprimeraletra==False:
            heecontradolaprimeraletra = True
        else:
            nueva+=j
    return nueva

def buscarletra(cadena,letra):
    cadena=minusculas(cadena)
    flag=False
    for i in cadena:
        if letra==i:
            flag=True
    return flag



def encontrar(cadena,escondida):
    for i in escondida:
        cadena=buscarletra(cadena,i)
    if cadenaAux==cadena:
        return False
    else:
        cadena 
        return True 

#Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y
#deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla por la
#tercera.

def buscaryreemplazar (cadena,letra1buscar,letracambiar):
    cadena=input("Introduce una frase")
    letrabuscar=input("que letra quieres buscar")
    letracambiar=input("por que letra la quieres cambiar")
    for i in range(len(cadena)):
        if buscarletra(cadena,letrabuscar)==True:
            resultado=letrabuscar=letracambiar
    return resultado

print(buscaryreemplazar("Jose","e","a"))
    
    
#Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
#otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
#al principio y todas las vocales al final de la misma, eliminando los blancos.
#Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería
#"crsdprgrmcnuoeoaaio

def consonantesyvocales(cadena):
    
    
    
    
    
    
#Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
#como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco.
#También al principio y al final de la frase puede haber blancos redundantes.
#Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    