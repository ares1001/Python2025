# Reto 5: Venta de entradas para un evento de tecnología,
# Un evento de tecnología vende entradas:
# Entrada normal: $8000.,
# Si la persona es estudiante (responde s/n), obtiene 50% de descuento.,
# El usuario se debe registrar por medio de su correo electrónico y puede indicar la cantidad de entradas,
# Además se tiene que verificar que el correo electrónico ingresado contenga "@" y termine en ".com". Si no es un correo válido, informar el error.
# Se debe mostrar el precio final.


mail=input("por favor ingrese su direccion de mail ").strip()

if "@" in mail and mail.endswith("com"):
    print("el mail es valido")
else:
    print(" el mail es incorrecto")
    exit()

estudiante=(input(" es usted estudiante (si/no):  ")).strip().lower()

cantidad=int(input("ingrese el numero de entradas que desea comprar ?"))
entrada = 8000

precio_final =0

if estudiante == "si":
    precio_final = entrada *0.5 * cantidad
else:
   precio_final= entrada*cantidad

print("el valor correspondiente a " , cantidad, "entradas es de " , precio_final)






    # print("El valor de la entrada es de ", entrada)