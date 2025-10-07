"""
FOR - Estructura repetitiva
sirve para repetir una cantidad de veces una accion
iterar acciones varias veces recorriendo elementos de una secuencia( lista, cadena, otros tipos de datos)
SINTAXIS

FOR variable_aux IN secuencia :
#bloque de acciones a repetir
#accion 1
#accion 2
#accion x
"""


shopping_list = ['Pan', 'Queso' , 'Jamon', 'Cafe']


for product in shopping_list:
    print(f"que tienes que comprar: {product}")



word = "python"
for letter in word :
    print(letter)


phrase ="me gusta programar en Python"
search_letter = input("ingrese caracter a contar :")
count = 0
for letter in phrase :
    if letter == search_letter:
        count += 1 #count _= count + 1
print(f"la letra {search_letter} aparece {count} veces")