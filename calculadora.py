fin= False

print("""************
Calculadora
************

Menu
1) Suma
2) Resta
3)Multiplicación
4)División
5)Salir""")

while not(fin):
    opc= int(input("Opción: "))
    if opc==1:
        sum1= int(input("Ingrese valor 1: "))
        sum2= int(input("Ingrese valor 2: "))
        print("La suma es: ",sum1+sum2)
    elif opc==2:
        res1= int(input("Ingrese valor 1: "))
        res2= int(input("Ingrese valor 2: "))
        print("La resta es: ",res1-res2)
    elif opc==3:
        mul1= int(input("Ingrese valor 1: "))
        mul2= int(input("Ingrese valor 2: "))
        print("La multiplicación es: ",mul1*mul2)
    elif opc==4:
        div1= int(input("Ingrese valor 1: "))
        div2= int(input("Ingrese valor 2: "))
        print("La división es: ",div1/div2)
    elif opc==5:
        fin=True
        print("Fin del programa")
