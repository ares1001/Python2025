"""
Scope de funciones
Determina donde es accesible una variable dentro del codigo
"""
#Scope local
def crear_usuario(nombre,email,activo=True):
    #Estado es una variable local
    print(f"Usuario: {nombre}")
    print(f"Email: {email}")
    if activo:
        estado = '🆗'
    else:
        estado = '❌'
    print(f"Estado: {estado}")

#Quiero llamar a una variable local por fuera de la funcion
#NameError ❌
#print(estado)

#Scope Global
mensaje_bienvenida = "Bienvenidos a la biblioteca"

def mostrar_mensaje():
    #Estoy usando la variable global (solo lectura)
    #mensaje_bienvenida = 'Modificando mensaje' -> si hago esto creo una variable local distinta la global
    #Si necesitamos modificar la variable globa
    #dentro de la funcion -> global
    global mensaje_bienvenida
    mensaje_bienvenida = 'Modificada en la funcion'
    print(f"Desde local: {mensaje_bienvenida}")

mostrar_mensaje()
print(f"Desde principal: {mensaje_bienvenida}")


"""
Manejo de variables mutables en scopes locales y globales
"""

books = ['El principito','el señor de los anillos']

def add_book(book):
    print("Agregando un libro")
    #VARIABLE GLOBAL
    books.append(book)
    print("Libro agregado exitosamente")

add_book('Harry potter')
print(books)

def add_book_v2(books,new_book):
    print("Agregando un libro")
    #Hace referencia al parametro
    books.append(new_book)
    print("Libro agregado exitosamente")

libros = ["Rayuela"]
add_book_v2(libros,"El quijote")
print(libros)