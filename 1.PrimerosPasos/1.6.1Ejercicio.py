# Ejercicio 1
# Crear un programa, que tenga una variable con la cadena “Tu nombre completo”, y muestre la siguiente información:
# • Imprima los dos primeros caracteres.
# • Imprima los tres últimos caracteres.
# • Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
# • Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
# • Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.

cadena="Juan Luis Bravo Velez"
# imprima los 2 primeros caracteres
print(cadena[:4])
#imprima los 3 ultimos caracteres
print(cadena[(len(cadena)-5):])
print(cadena[-5:])
# imprima dicha cadena cada 2 caractres
print(cadena[::4])
# Imprima en sentido inverso la cadena
print(cadena[::-1])
print(cadena+cadena[::-1])



