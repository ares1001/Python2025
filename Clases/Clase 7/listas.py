"""
LISTAS
"""
animals_list = ["perro","vaca","gato","jirafa"]

#ordenado
# print(animals_list[1])
# print(animals_list[2])

# #recorrido de una lista
for animal in animals_list:
    print(f"Animal: {animal}")

# #OPERACIONES con lista
# #agregar al final de una lista
# animals_list.append("🐍")
# print(animals_list)

# #Insertar un valor en un posicion
# animals_list.insert(2,"🐘")
# print(animals_list)

# #Eliminar elementos de la lista por medio de un valor
# animals_list.remove("perro")
# print(animals_list)

# #Eliminar de acuerdo a una posición
# del animals_list[2]
# print(animals_list)

# #POP: elimina y devuelve el elemento de acuerdo al indice
# removed_animal = animals_list.pop(1)
# print(animals_list)
# print(f"Animal extraido: {removed_animal}")

# # print(f"Animal extraido: {animals_list.pop(1)}")
# # print(animals_list)

# #Devuelve la posición de un elemento dado su valor
# index_animal = animals_list.index("jirafa")
# print(f"Jirafa en la posición: {index_animal}")

# animals_list.append("vaca")
# animals_list.append("vaca")
# print(animals_list)
# #Contar la cantidad de elementos en base a un valor
# print(animals_list.count("vaca"))

# print(f"Cantidad de animales: {len(animals_list)}")

# #Cadenas y podemos dividirlas en listas
# fruits = "banana,manzana,pera,sandia"
# print(fruits)
# fruits_list = fruits.split(",") # "," es el separador
# print(fruits_list)
# email = "fede@gmail.com"
# domain = email.split("@")
# print(domain)

# #Unir los elementos de una lista a una cadena
# product_list = ['pan','aceite','leche'] #Lista
# # "; " es la cadena por medio de la cual quiero unir los elementos de la lista
# products_string = " ".join(product_list)
# print(products_string)



