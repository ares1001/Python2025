"""
Slicing nos permite dividir una secuencia ( lista/ tupla) de elementos
en partes
Sintaxis
secuencia[inicio:fin:salto]
inicio : posicion donde empieza el corte
fin : posicion donde termina el corte ( no incluye ese indice)
salto ( opcional) : cada cuantos elementos va a saltar
"""

numbers = [10,50, 67, 89, 100, 99, 44, 66]
sublist = numbers[1:4] # indicando un inicio y un fin

print(f"Sublist : { sublist}")

sublist_1=numbers[2:]  # indicando un inicio
print(f"Sublist_1: {sublist_1}")

sublist_2 = numbers[1:7:2] #indicando inicio fin y salto
print(f"Sublist_2{sublist_2}")

#Obtener la lista en un orden inverso 
sublist_3 = numbers[::-2]
print(f"Sublist_3{sublist_3}")

#Tuplas pasa igual 
weekdays = ("lunes", "martes", "miercoles", "jueves","viernes")
print(weekdays[1:3])

"""
COPIAR UNA LISTA
"""
list_names =["Caro", "Fernando", "Ariel"]

"""
Esta forma no es la indicada para hacer una copia de la lista
la asignacion solo hace referencia a la posicion de memoria 
de la variable original

Los cambios que haga en la variable copia en definitiva se hacen en la 
referencia de la lista original
list_names_copy = list_names

list_names_copy.append("Pablo")

"""

list_names_copy = list_names[:]
list_names_copy.append("Patricia")
print(f"Copia : {list_names_copy}")
print("")
print(f"Original : {list_names}")

#opcion 2 usando una funcion copy()
list_names_copy_2 = list_names.copy()
list_names_copy_2.append("Dante")
print(f"Copia 2 : {list_names_copy_2}")
print(f"Original : {list_names}")