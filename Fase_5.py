print("---Cadenas de texto (Avanzado)---")

cadena= "en un lugar de la mancha..." #la 1º en may
print(cadena.capitalize())

cadena= "en un lugar de la mancha..." #todo en may
print(cadena.upper())

cadena= "EN UN LUGAR DE LA MANCHA..." #todo en min
print(cadena.lower())

cadena= "en un lugar de la mancha..." #longitud de los caracteres
print(len(cadena))
print("----------------------")

cadenaejemplo = "En un lugar de la mancha..." #comprueba si los caracteres son alfanumericos o no.
print(cadenaejemplo.isalnum())
cadenaejemplo = "1234567890"
print(cadenaejemplo.isalnum())
cadenaejemplo = "abcdefg1234567890"
print(cadenaejemplo.isalnum())
cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isalnum())
print("----------------------")

cadenaejemplo = "Enunlugardelamancha"  #comprueba que todos sean alfabéticos
print(cadenaejemplo.isalpha())
cadenaejemplo = "En un lugar de la mancha"
print(cadenaejemplo.isalpha())
cadenaejemplo = "1234567890"
print(cadenaejemplo.isalpha())
cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isalpha())
print("----------------------")

cadenaejemplo = "En un lugar de la mancha" #comprueba si todos son numéricos
print(cadenaejemplo.isdigit())
cadenaejemplo = "1234567890"
print(cadenaejemplo.isdigit())
cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isdigit())

cadenaejemplo = "En un lugar de la mancha" #comprueba si todos están en minusculas
print(cadenaejemplo.islower())
cadenaejemplo = "en un lugar de la mancha"
print(cadenaejemplo.islower())
print("----------------------")

cadenaejemplo = "En un lugar de la mancha" #comrueba si todos están en mayusculas
print(cadenaejemplo.isupper())
cadenaejemplo = "EN UN LUGAR DE LA MANCHA"
print(cadenaejemplo.isupper())
print("----------------------")

cadenaejemplo = "En un lugar de la mancha" #elimina espacios al principio y al final
print(cadenaejemplo.lstrip()) #principio
cadenaejemplo = "En un lugar de la mancha "
print(cadenaejemplo.rstrip()) #final
cadenaejemplo = " En un lugar de la mancha "
print(cadenaejemplo.strip()) #ambos

print("----------------------")
cadenaejemplo = "abcdefghijklmnopqrstuvwxyz" #permitirte conocer el carácter alfabético
                                             #mayor y menor de la cadena de texto.
print(max(cadenaejemplo))
print(min(cadenaejemplo))

print("----------------------")

cadena="AEIOU"
print(cadena.replace("A","E"))
