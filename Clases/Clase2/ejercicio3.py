nombre_producto = input("ingrese el nombre de tu producto")
precio= float(input("ingrese el precio de venta"))
cantidad=int(input("ingrese cuantos vendio"))

total = precio*cantidad

factura = " el saldo a pagar es $ " + str(total)
print(factura)
