# 2. Operadores LÓGICOS
num1 = 50
num2 = 10
num3 = 150
num4 = 150

print("\nOPERADOR and") 
print((num1>num2) and (num3<=num4)) # TRUE  and TRUE  ==> TRUE
print((num1>num2) and (num3<num4))  # TRUE  and FALSE ==> FALSE
print((num1<num2) and (num3<=num4)) # FALSE and TRUE  ==> FALSE
print((num1<num2) and (num3<num4))  # FALSE and FALSE ==> FALSE

print("\nOPERADOR or")
print((num1>=num2) or (num3==num4)) # TRUE  or TRUE  ==> TRUE
print((num1>num2)  or (num3<num4))  # TRUE  or FALSE ==> TRUE
print((num1<=num2) or (num3<=num4)) # FALSE or TRUE  ==> TRUE
print((num1<num2)  or (num3>num4))  # FALSE or FALSE ==> FALSE

print("\nOPERADOR not")
print((not num1<num2) or (num3<num4)) # notFALSE or FALSE ==> TRUE
