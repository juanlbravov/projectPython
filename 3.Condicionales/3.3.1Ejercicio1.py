# Ejercicio 1
# Crear un programa que pida al usuario una letra, y si es vocal, 
# muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

letra = input ("por favor ingrese una letra: ")
letraminuscula = letra.lower()

if letraminuscula in "aeiou":
    print("la letra {} SI es una vocal".format(letra))
else:
    print("la letra {} NO es una vocal".format(letra))

