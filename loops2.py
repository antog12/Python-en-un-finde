language = 'Python'
for letter in language:
    print(letter)

print("-------------")

for i in range(len(language)):  # igual que el de arriba
    print(language[i])


print("tuplas")

numbers = (0,1,2,3,4,5)

for number in numbers:
    print(number)


print("Diccionarios")

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key in person.items():  # me muestra las claves y el valor en el for
    print(key)

print("------------------------------")

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

print("Romper y continuar")

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
print("------------------------------")

for number in numbers:
    print(number)
    if number == 3:
        continue
    print("El ss num debería de ser ", number+1) if number != 5 else print("fin del loop")
print("fuera del loop")

print("rangos")

list= list(range(1,11))
print(list)