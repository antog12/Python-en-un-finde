print("FASE 1: Uso de una función")

def Saludar():
    print("Hola Mundo")
Saludar()

print("---------------------")

def EsMayorQueCero(param):
    if param>0:
        print("El parametro es mayor que cero")
    else:
        print("El parametro es menor que cero")
numero= int(input("introduce un número: "))
EsMayorQueCero(numero)  #número es el parámetro que le paso.


print("---------------------")

def sumar(param1,param2):
    return param1 + param2
num1= int(input("introduce el primer num: "))
num2= int(input("introduce el segundo num: "))
resultado= sumar(num1,num2)
print("El resultado de la suma es: ",resultado)

print("---------------------")

def SumaResta (param1, param2):
    return param1 + param2, param1 - param2
num1= int(input("introduce el primer num: "))
num2= int(input("introduce el segundo num: "))
resultadoSuma, resultadoResta= SumaResta(num1,num2)
print("El resultado de la suma es: ",resultadoSuma)
print("El resultado de la resta es: ",resultadoResta)

print("---------------------")
def sumar(*valores):
    resultado=0
    for item in valores:
        resultado=resultado + item
    return resultado
resultado=sumar(23,56,3,87,78,455)
print("El resultado de la suma es: ",resultado)

print("---------------------")

def nombreCompleto ():
    nombre= "Antonio"
    apellido= "Abellán"
    espacio= " "
    fullName= nombre + espacio + apellido
    print (fullName)
nombreCompleto()

print("---------------------")

def nombreCompleto ():
    nombre= "Antonio"
    apellido= "Abellán"
    espacio= " "
    fullName= nombre + espacio + apellido
    return fullName
print(nombreCompleto())



