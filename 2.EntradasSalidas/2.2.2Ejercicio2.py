# Ejercicio 2
# Hacer un programa que 
# pida al usuario su nombre, edad y sexo
# muestre la información así:
#   te llamas: <nombre>
#   tu edad es: <edad>
#   tu sexo es: <sexo>
# nota: de momento no entraremos en comprobaciones o conrol de fallos

nombre = input("por favor indica tu nombre: ")
edad = int(input("por favor indica tu edad: "))
sexo = input("por favor indica tu sexo: ")

print("\nte llamas: {}\ntu edad es: {}\ntu sexo es: {}".format(nombre,edad,sexo))
