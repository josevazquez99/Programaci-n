#Design a function called charactersInString that has a character string and a character as
#input parameters and returns how many times that character appears in the string. It should
#do if the string and character are lower case or upper case characters.
from pickle import TRUE
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
    for i in range (len (cadena)):
        if minusculas(cadena[i]) == True:
            cadena[minusculas(cadena[i])==True]=minusculas(cadena[i])==False
    return cadena
        
print (mayuscula("Jose"))
    