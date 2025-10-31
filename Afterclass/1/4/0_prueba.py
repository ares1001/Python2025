#Reto 1: Calculadora de vuelto,
#Un cliente compra un producto. Ingresá el precio y la cantidad entregada por el cliente.
#Si entregó menos del precio, indicar que falta dinero. Si entregó lo justo, decir "Pago exacto".
 #Si sobró, informar el vuelto.




producto = "arroz"
precio =(int(1200))
print(" el precio del kilo de " , producto," es de ", precio)

pago_cliente= (int(input(" ingrese el monto a pagar $ ")))


if pago_cliente < precio:
    falta = precio - pago_cliente
    print(" restan por pagar" , falta)
elif pago_cliente == precio:
    print(" Gracias por su compra")
else:
    vuelto = pago_cliente - precio
    print( " su vuelto es $" , vuelto)



