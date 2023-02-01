print("FASE 1: Bucle WHILE")

i=0
while i<10:
    print(i, end=" ")
    i=i+1

print("------------------------")

continuar=True
while continuar:
    valor= int(input("ingrese un número superior a 100: "))
    if valor>100:
        continuar=False
print("programa terminado")

print("------------------------")

print("FASE 2: Bucle FOR")

lista=[1,2,3,4,5,6,7,8,9]
for item in lista:
    print(item, end=" ")

print("/n")
print("------------------------")

lista = ["ordenador", "teclado", "raton"]
for item in lista:
    print(item, end=" ")

print("/n")
print("------------------------")


for item in range(10):
    print(item, end=" ")

print("/n")
print("------------------------")
print("FASE 3: Bucles anidados")

for item1 in range(3):
    for item2 in range(5):
        print("item1 = " + str(item1) + ", item2 = " + str(item2))


print("/n")
print("------------------------")

item1 = 0
while item1<3:
    for item2 in range(5):
        print("item1 = " + str(item1) + ", item2 = " + str(item2))
    item1 = item1 + 1






