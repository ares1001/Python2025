# Reto 6: Verificación de descuento en supermercado
# Un cliente recibe un 10% de descuento si es mayor de 60 años
# o si es cliente habitual.
# ENTRADA: edad (int) - cliente_habitual (str / boolean)


edad = int(input("Ingrese su edad"))
cliente=bool(input(" es socio de nuestras cadenas? (s/n)").lower() =="s")

if edad > 60 or cliente:
    print(cliente)
    print("tienes un 10% de descuento")
else:
    print("no podes acceder a nuestros descuentos")