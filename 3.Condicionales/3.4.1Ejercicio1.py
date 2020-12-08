# Ejercicio 1
# Escribe un programa que pida dos palabras y diga si riman o no.
# Si coinciden las tres últimas letras tiene que decir que riman.
# Si coinciden sólo las dos últimas tiene que decir que riman un poco
# y si no, que no riman.

palabra1 = input("Palabra1 = ")
palabra2 = input("Palabra2 = ")

if len(palabra1)<3 or len(palabra2)<3:
    print("Las palabras definidas deben tener mínimo 3 caracteres")
else:
    print("aqui voy")

