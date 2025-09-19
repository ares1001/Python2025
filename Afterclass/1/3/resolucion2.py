# Reto 2: Verificación para donar sangre
# Una persona puede donar sangre si tiene entre 18 y 65 años inclusive y
# pesa más de 50 kg.
# ENTRADA: edad (int) - peso en kg (float)
# PROCESO: conversiones - verificar condición para donar sangre
# SALIDA: mensaje (str)



edad = int(input("ingrese su edad"))
peso = float(input("ingrese su peso en (kg)"))


if edad >= 18 and edad <=65 and peso >50:
# if 18 <= edad <= 65 and peso > 50:
    print("puede donar sangre")
else:
    print(" No puede donar sangre")    
