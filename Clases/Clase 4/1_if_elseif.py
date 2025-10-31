"""
IF-ELIF - ELSE
verifica condciones multiples secuenciales
"""

"""
Ejemplo 1 , descuento por cantidad de productos 
productos >= 10 -> 20% Descuento
5 <= productos <10 -> 10% Descuento
productos <5 -> no tiene descuentos
solo hay descuentos si se paga por MP
"""
paga_con_qr =True
cantidad_productos =int(input("ingrese la cantidad de productos"))


if paga_con_qr:
    if cantidad_productos >= 10 :
        print("Le corresponde un 20% de descuento")
    elif cantidad_productos >= 5  :
        print("le corresponde un 10 de descuento")
 
    elif cantidad_productos > 0:
        print("no tiene descuento")

else:
    print(" caracter no admitido") 



print("Gracias por tu compra")


"""
IF ANIDADOS
simular doble autenticacion

"""


# usuario = input("Ingrese usuario: ")
# contrasenia = input("Ingrese su pass: ")


# if usuario == 'admin' and contrasenia == '123456':
#     print("acceso valido")
#     codigo_seguridad= input("ingrese el codigo enviado")
#     if codigo_seguridad=='g-1234':
#         print("Bienvenido")
#     else:
#         print("codigo incorrecto")
# else:
#     print("datos incorrectos")
