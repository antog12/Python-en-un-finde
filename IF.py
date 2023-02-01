print("---FASE 1: Sentencia IF---")

numero= int(input("Escribe un número: "))
if numero > 10:
    print("El número que has escrito es mayor que 10!!")
print("Has escrito el número: ", + numero)
print("----------------")
print("FASE 2: Sentencia IF..ELSE")

cadena= "En un lugar de la mancha.."
if "lugarr" in cadena:
    print("Encontrado!!")
else:
    print("No encontrado")

print("----------------")

cadena= "En un lugar de la mancha"
if cadena.startswith("E"):
    print("Empieza por E!!!")
else:
    print("No empieza por E!")
if cadena.endswith("P"):
    print("Termina por P!!!")
else:
    print("No termina por P!!")

print("----------------")
print("FASE 3: Sentencia IF..ELIF..ELSE")

import random

num1= random.randint(0,10)
num2= random.randint(0,10)
print(num1)
print(num2)

if num1 > num2:
    print("num1 es mayor que num2")
elif num1==num2:
    print("LOs números son iguales")
else:
    print("el num1 es menor que el num2")


