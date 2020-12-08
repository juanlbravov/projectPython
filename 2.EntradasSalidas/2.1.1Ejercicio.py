# Ecuaciones de 2do grado
#
#     -b +- raiz(b^2 - 4ac)
# x = _____________________  ==> 3x^2-5x+2=0  
#            2a
# 
# ==> a=3  b=-5  c=2
# obtengo x1=1 x2=2/3

from math import sqrt  # libreria math para raices cuadradas

a = int(input("añade valor de a: "))
b = int(input("añade valor de b: "))
c = int(input("añade valor de c: "))

x1 = 0 # definimos valor positivo
x2 = 0 # definimos valor negativo

raiz = ((b**2) -(4*a*c))
print ("raiz:", raiz)

if raiz < 0:
    print ("no se puede realizar, las raices cuadradas no pueden ser de numeros negativos")
else:
    x1 = (-b + sqrt(raiz)) / (2*a)
    x2 = (-b - sqrt(raiz)) / (2*a)
    print ("La solucion es: \n x1=",x1,"\n x2=",x2)
