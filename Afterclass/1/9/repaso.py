#REPASO SCOPE LOCAL - GLOBAL
libro_destacado = 'El principito' # <- Aqui la variable es global

def obtener_libro_destacado():
    libro_destacado = 'Rayuela' # <- crear una referencia a una variable local distinta a la global
    print(f"El libro destacado (dentro de la funcion) es: {libro_destacado}")

def obtener_libro_destacado_v2():
    global libro_destacado # <- indicabamos que ibamos a usar la variable GLOBAL QUE ES INMUTABLE
    libro_destacado = 'Harry potter'
    print(f"El libro destacado (dentro de fn v2) es: {libro_destacado}")

#Ejemplo scope local
#obtener_libro_destacado()
#print(libro_destacado)

# Ejemplo modificacion de scope global
#obtener_libro_destacado_v2()
#print(libro_destacado)

def obtener_libro_descatado_v3(libro=""):
    libro = 'El quijote'
    print(f"El libro destacado (dentro de fn 3) es: {libro}")
    return libro

libro_destacado = obtener_libro_descatado_v3(libro_destacado)
print(libro_destacado)



#CASOS ESPECIALES DE VARIABLES GLOBALES MUTABLES

products = ['Pan','Cafe']

def add_product():
    #Variable local
    #products = []  #NO VA A PASAR: intento limpiar la lista de productos globales
    product = input('Ingrese nombre de producto:')
    #Usando variable GLOBAL MUTABLE
    products.append(product)
    print("Producto agregado exitosamente")

# Ejemplo 1
# print(products)
# add_product()
# print(products)

def add_product_v1(products):
    """SOLUCION 1: Paso como parametro la lista que queiro modificar"""
    product = input('Ingrese nombre de producto:')
    #Usando variable GLOBAL MUTABLE
    products.append(product)
    print("Producto agregado exitosamente")

#Ejemplo 2
add_product_v1(products)
print(products)

productos_vencidos = ['leche','queso']
add_product_v1(productos_vencidos)
print(productos_vencidos)


def add_product_v2(products):
    """SOLUCION 2: Paso como parametro la lista que queiro modificar
        Se hace el return explicito de la lista modificada
    """
    product = input('Ingrese nombre de producto:')
    #Usando variable GLOBAL MUTABLE
    products.append(product)
    print("Producto agregado exitosamente")
    return products

#variable global
productos_nuevos = ['remera','pantalon']
productos_nuevos = add_product_v2(productos_nuevos)
print(productos_nuevos)