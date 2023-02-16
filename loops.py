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

print("------------------------")

count = 0

while count < 5:
    print(count)
    count = count + 1
else:
    print(count) # cuneta el 5

print("------------------------")

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count== 3:
        print("para en el 3")
        break

print("------------------------")

count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1

print("------------------------")

numbers = [0, 1, 2, 3, 4, 5]

for number in numbers:
    print(number)

print("------------------------")


language = 'Python'
for letter in language:
    print(letter)













