# Reto 4: Clasificación de paquetes de envío,
#Una empresa de envíos clasifica paquetes por peso: 
#Menos de 2 kg: "Ligero".,
#Entre 2 kg y 10 kg: "Estándar".,
#Más de 10 kg: "Pesado".,
#Además si el cliente tiene un código de descuento válido ("ENVIO10"),
#se aplica un 10% de descuento sobre el costo base de $1000.
#Calcular y mostrar el precio final.



peso_paquete = int(input("Cuanto pesa su envio en kilogramos  ?"))
envio =int(1000)
cupon= input("tiene un cupon de descuento ( o deje vacio si no tiene):").strip().upper()

if peso_paquete < 2 :
    print(" su envio es catalogado como ligero")
elif 2<=  peso_paquete >=10:
    print(" su envio es catalogado como estandar")
else:
    print("su envio es catalogado como pesado")

if cupon =="ENVIO10":
    precio_envio= envio * 0.9
else:
    precio_envio = envio

print("el costo del envio es de : $ " , precio_envio)
