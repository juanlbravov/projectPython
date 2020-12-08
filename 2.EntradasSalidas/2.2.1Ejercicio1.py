# Ejercicio 1
# escribe un programa que pida una vocal en minuscula y una letra en mayuscula
# debe convertir la vocal a mayuscula y la letra a minuscula e imprimir ambas concatenadas
# nota: de momento no entraremos en comprobaciones o conrol de fallos

vocal = input("Ingrese una vocal en minuscula: ")
letra = input("Ingrese una letra en mayuscula: ")

print ("tu vocal es {} y tu letra es {} y la combinación de ambas es {}".format(vocal.upper(), letra.lower(),vocal.upper()+letra.lower()))