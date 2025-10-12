"""
TUPLAS
Similar a la listas, con la diferencia principal
son INMUTABLES, una vez creadas NO PUEDE MODIFICARSE
"""

my_list = ['Fede','Liquin']
my_tuple = (10, 20, 'un texto', True, my_list )
print(my_tuple[4])
#my_tuple[3] = 'Otro texto' #Error porque no no puedo cambiar un elemento

#Asignacion multiple por medio de una tupla
x, y, z = 20,5,77
print(x)
print(y)
print(z)

#Tupla de colores
colors = ("rojo","verde","azul")
print(type(colors))
#colors.append('amarillo') No esa  definida la funcion append
for color in colors:
    print(f"Color: {color}")


week_day = "lunes","miercoles","viernes"
numbers = 23,67,23


domains = ("bue.edu.ar","gmail.com","yahoo.com","outlook.es")
print(domains)
email = input("INgrese su correo electronico: ")
if email.endswith(domains):
    print("correo valido")
else:
    print("Correo no valido")

number_list = [14,565,45]
numbers_tuple = tuple(number_list)
print(type(numbers_tuple))


