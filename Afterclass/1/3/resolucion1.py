# Reto 1: Control de acceso al gimnasio
# Solicitar al usuario su edad y si tiene una suscripción activa.
# Solo puede ingresar al gimnasio si tiene al menos 16 años y
# tiene la suscripción al día.

# Entrada: edad (entero) y suscripcion (str / boolean)
# Proceso: conversión - determinar acceso al gimnasio cumpliendo condiciones
# Salida: mensaje (str)


edad = int(input("Ingrese su edad"))
activo= input("Tiene su suscripcion al dia ?(s/n):").lower()

if edad >=16 and (activo =="s"):
    print(" puedes ingresar")
else:
    print("debes renovar tu suscripcion")

