#cadena replace

cadena="Separado"
i = 0
tamanio=len(cadena)
imprimo = ""

while i < (tamanio):
    obtengo = ((cadena[i::tamanio]))
    imprimo += str(obtengo) + ','
    i += 1

print(str(imprimo))

