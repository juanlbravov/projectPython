# Ejercicio 2
# Crear un programa que permita al usuario elegir un candidato por el cual votar. 
# Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
# Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.
# Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula

print("Elija un candidato por el cual votas.\nLas posibilidades son:\ncandidato A por el partido rojo,\ncandidato B por el partido verde,\ncandidato C por el partido azul.")
candidato = input("indique candidato: ")

if candidato.upper()=="A":
    print("\nUsted ha votado por el partido rojo")
elif candidato.upper()=="B":
    print("\nUsted ha votado por el partido verde")
elif candidato.upper()=="C":
    print("\nUsted ha votado por el partido azul")
else:
    print("\nOpción errónea")