#Reto 2: Control de ingreso a parque de diversiones,
#Un niño puede subir a una atracción si mide más de 1.20 metros.
#Si mide menos, pero tiene más de 10 años, también se le permite.
#Calculá además el precio del pase, que es $2500 y tiene un 20% de descuento
#  si el niño tiene un cupón



altura = float(input("Bienvenidos a la sky revolution, ingrese su altura en cm "))
edad = int(input(" ahora ingrese su edad "))
entrada = 2500
cupon= input("tiene un cupon de descuento (si/no):").strip().lower()

if altura> 120 :
    print(" puede subir")
elif altura <= 120 and edad>10:
    print(" puede subir igual")
else:
    print(" no puede subir")


if cupon == "si":
    precio_entrada = entrada * 0.8
else:
    precio_entrada = entrada

print(" el precio de la entrada es : $ ", precio_entrada)
