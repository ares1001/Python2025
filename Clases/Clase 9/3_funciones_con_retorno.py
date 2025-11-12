"""
Funciones con retorno
Estas funciones devuelven un resutado usando
la palabra reservada return
"""

def generar_usuario(nombre,apellido):
    usuario = nombre[0] + apellido
    return usuario

nuevo_usuario = generar_usuario("Patricia","Romero")
print(nuevo_usuario)

print(f"Nuevo usuario: {generar_usuario('ramiro','Ramirez')}")