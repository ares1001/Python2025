"""
Cadneas o STR secuencia de caracteres '' o "" 


"""

cadena_1="Hola mundo"
cadena_2="estudiando Python"
cadena_3 = """ Esto es una cadena de 
Menu
1-esta es una cadena
2 de multiples
3. lineas
4. lalalal
"""


print(cadena_1)
print(cadena_2)
print(cadena_3)


#Operaciones con cadenas

saludo="Hola "
nombre="Ariel"

mensaje=saludo+ " " + nombre
print(mensaje)

#Repeticion
parte_1 ="Na " * 8
print(parte_1)


frase = parte_1 + " Batman "
print(frase)

#longitud de la cadena
longitud= len(frase)
print(longitud)

#comprobar si una cadena esta dentro de otra IN

existe = "python" in cadena_2
print(existe)


#Metodo de cadenas

mensaje_dos="Hola comision 25204 Python"
print(mensaje_dos.upper())
print(mensaje_dos.lower())