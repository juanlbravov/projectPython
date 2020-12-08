# Ejercicio 2
# Crear un programa que tenga una variable con la cadena “TextoSeparado” y un carácter de coma(,) e inserte el carácter entre cada letra de la cadena. 
# Ejemplo si el texto es "separar" debería devolver s,e,p,a,r,a,r,
# Pista: recuerda que la posición de los caracteres empieza en 0.

cadena="TextoSeparado"
i = 0
tamanio=len(cadena)
imprimo = ""

while i < (tamanio):
    obtengo = ((cadena[i::tamanio]))
    imprimo += str(obtengo) + ','
    i += 1

print("texto a imprimir es ==> ",str(imprimo))

