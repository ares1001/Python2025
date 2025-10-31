"""


RANGOS-RANGE

funcion que incluye Python 
permite generar una SECUENCIA de NUMEROS ENTEROS
Esta secuencia puede ser recorrida en un FOR
Sintaxis
range(fin) # Fin indica el numero final de la secuencia, no lo incluye


"""

print(type(range(6)))
print(range(6))



# indicar el numero final , pero no lo incluye
for numeros in range(20):
    print(numeros)


#range(inicio, fin)

for num in range(3,8):
    print(f"los numeros comprendidos son {num}")

#range(inicio , fin, paso)
#permite definir el paso 

# print("-"*30)

# n =int(input( "ingrese un valor"))
# for i in range (10,21,n):
#     print(f"Rango con paso : {i}")


for n in range(20,10, -1):
    print(f"Valor del rango con paso : {n}")


print("-"*30)

shopping_list = ['Pan', 'Queso' , 'Jamon', 'Cafe', 'Medialunas']
# new_product = input("ingrese producto ")
# shopping_list.append(new_product)


len_shopping_list =len(shopping_list)
for index in range(len_shopping_list):
    #for index in range(len(shopping_list))
    
    print(f"que tienes que comprar: {index+1} :{shopping_list[index]}")


print("-"*30)
product_search = input("Ingrese producto a buscar")
for index in range(len_shopping_list):
   if shopping_list[index] == product_search:
    
    print(f"Producto encontrado en posicion : {index}")
    break
