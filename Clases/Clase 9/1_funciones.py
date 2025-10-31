"""
Funciones es un bloque de codigo reutilizable que realiza
UNA TAREA ESPECIFICA.

Sintaxis básica:

def nombre_funcion():
    accion1
    accion2
    accion3
    ...
    accionX

invocacion desde el programa principal o desde donde quiera
utilizarla

nombre_funcion()

nombre_funcion()

nombre_funcion()
"""
def mostrar_bienvenida():
    print("Buen dia ")
    print("Bienvenido al sistema de gestión de biblioteca TT 📚")

#llamada la funcion o invocación
mostrar_bienvenida() #print("Bienvenido al sistema de  biblioteca TT")

"""
FUNCIONES CON PARAMETROS
"""
def registrar_libro(titulo,genero, copias):
    """
    Tanto titulo y genero son parametros definidos para la funcion
    """
    print("Agregando un libro")
    print(f"Titulo: {titulo}")
    print(f"Genero: {genero}")
    copias = copias + 1
    print("Libro agreado exitosamente")
    print("")

#llamar a la función -> argumentos
registrar_libro("El principito","Cuento infantil",1)
registrar_libro("Harry potter","Fantasía",2)
#Tener con el orden de los argumentos
#registrar_libro("Novela",3,"Cien años de soledad")

#Tener cuidado con la cantidad de argumentos
#Debe ser igual a la cantida de parametros definidos
#registrar_libro("El señor de los anillos","Novela")

"""
Funciones con parametros con valores por defecto
"""
def agregar_libro_v2(titulo,genero="Novela",copias=1):
    #copias recibe por defecto el valor 1 en
    # caso de no ser enviada
    print("Agregando un libro")
    print(f"Titulo: {titulo}")
    print(f"Genero: {genero}")
    print(f"Copias: {copias}")
    print("Libro agreado exitosamente")
    print("")

agregar_libro_v2("El alquimista","Novela")
agregar_libro_v2("Don quijote")