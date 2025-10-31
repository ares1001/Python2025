"""
f-string
"""

nombre = 66
saludo = f"Hola, {nombre}!"
# saludo_normal = "Hola, " + nombre + "!"
print(saludo)



numero = 1
numero_2 = 55
resultado =f"el resulado es : {numero + numero_2}"
print(resultado)


ingreso = 60000
edad = 25 

if ingreso< 50000 :
    print("Ingresos bajos")
elif edad < 30:
    print("Joven con buenos ingresos")
else:

    print("adulto con buenos ingresos")


texto = "Hola Python"
print(len(texto))



texto = "Python"
print (texto.endswith("on"))


# dia =input("ingrese un dia de la semana")
# match dia :
#     case "Lunes" :
#         print("Inicio de semana")
#     case "Viernes":
#         print("Fin de semana")
#     case _:
#         print("dia intermedio")



match 10: 
    case 5:
        print("Cinco")
    case 10:
        print("Diez")
    case _:
        print("Otro numero")




email ="python@gmail.com"
print(email.endswith("gmail.com"))
print(email.startswith("py"))


texto = " estudiando python con cadenas , python"
nuevo_texto =texto.replace("python" , "Javascript", 2
                           )
print (nuevo_texto)


# edad = int(input("ingrese su edad"))
# if edad <= 18 :
#     print("menor")
# else:
#     print("mayor")


texto="Python"
print (texto.strip().upper())


texto = "Hola"
texto= "J"
print(texto)