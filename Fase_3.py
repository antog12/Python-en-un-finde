# Colecciones
print("---LISTAS---")

lista= ['ordenador', 'teclado', 'raton']
print(lista)

print("----------------------")

lista2= ['ordenador', 'teclado', 'raton']
print(len(lista2))
print(lista2[0])
print(lista2[1])
print(lista2[2])

print("----------------------")

listaoriginal= ['ordenador', 'teclado', 'raton']
nuevalista= ['monitor', 'impresora', 'altavoces']
listafinal= listaoriginal+nuevalista
print(listafinal)

print("----------------------")

lista3= ['ordenador', 'teclado', 'raton']
lista3.append('mesa')
print(lista3)

print("----------------------")
lista4= ['ordenador', 'teclado', 'raton']
print(lista4)
lista4[0]= 'monitor'
lista4[1]= 'impresora'
lista4[2]= 'altavoces'
print(lista4)


print("----------------------")

lista5= ['ordenador', 'teclado', 'raton']
print(lista5)
del lista5[1]
print(lista5)

print("----------------------")

listaprin= ['ordenador', 'teclado', 'raton',['tarjeta de sonido', 'micrófono', 'altavoces']]
print(listaprin[0])
print(listaprin[1])
print(listaprin[2])
print(listaprin[3])
print(listaprin[3][0])
print(listaprin[3][1])
print(listaprin[3][2])

print("---TUPLAS---")  #son inmutables

tupla= ('ordenador', 'teclado', 'raton')
print(tupla)
print(len(tupla))
print(tupla[0])
print(tupla[1])
print(tupla[2])


print("---DICCIONARIOS---") #colecciones de elementos compuestos por clave valor. Las claves no se pueden repetir

mesestraducidos= {"enero" : "january",
                  "febrero" : "february",
                  "marzo" : "march",
                  "abril" : "april",
                  "mayo" : "may",
                  "junio" : "june",
                  "julio" : "july",
                  "agosto" : "august",
                  "septiembre" : "september",
                  "octubre" : "october",
                  "noviembre" : "november",
                  "diciembre" : "december"}

print(mesestraducidos['noviembre'])
print(mesestraducidos['febrero'])
print(mesestraducidos['enero'])

