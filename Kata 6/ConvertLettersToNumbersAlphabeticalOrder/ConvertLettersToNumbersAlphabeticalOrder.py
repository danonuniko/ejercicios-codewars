"""
Kata Level: 6.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example:
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
"""

def alphabet_position(text):
    #Creamos el diccionario con los valores correspondientes a cada letra.
    alfabeto = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
    texto = text.lower()	#Pasamos el texto a minusculas.
    resultado = ""			#En esta variable guardaremos nuestro resultado final.
    for letter in texto:	#Recorremos el texto en minusculas.
        if letter in alfabeto:	#Manera de confirmar si la letra es una clave del diccionario.
            resultado += str(alfabeto.get(letter)) + " "	#En caso de que el simbolo sea clave del diccionario, añadimos al resultado el valor de dicha clave.
            
    return resultado[:-1]	#Eliminamos del resultado el último espacio en blanco.

print(alphabet_position("The sunset sets at twelve o' clock."))