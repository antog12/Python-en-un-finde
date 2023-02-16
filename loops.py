#while


my_conditio= 0

while my_conditio < 10:
    print(my_conditio)
    my_conditio += 2
if my_conditio == 10:
    print("mi condicion es igual a 10")
else:
    print("el valor es mayor o igual que 10")

print("------------------------")

while my_conditio < 20:
    my_conditio += 1
    if my_conditio ==15:
        print("se detiene la ejecución")
        break

    print(my_conditio)


print("------------------------")

my_list= [35,24,62,52,30,30,17]

for element in my_list:
    print(element)

print("------------------------")

my_tuple= (35, 1.77,"Antonio", "Angel", "Abellán")
for element in my_tuple:
    print(element)
    if element == "Angel":
        continue  #continua para continuar y break para parar
    print("Se ejecuta")
else:
    print("el bucle for ha finalizado")