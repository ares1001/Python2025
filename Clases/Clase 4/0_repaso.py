"""
CONDICIONAL IF-ELSE 
"""


nombre = input("ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))

# if nombre == "" or edad < 18:  #evaluamos la condicion

#     #Condicion es verdadera
#     print("error, datos incorrectos")

# else :
#       #si la condicion es falsa
#     print("***** Bienvenida")
#     print("Nombre :",nombre)
#     print("Edad : " , edad)
#     print("*********")


if nombre != "" and edad >= 18:  #evaluamos la condicion
    #Condicion es verdadera
    print("***** Bienvenida")
    print("Nombre :",nombre)
    print("Edad : " , edad)
    print("*********")
else :
      #si la condicion es falsa
     print("error, datos incorrectos")

print("Fin del programa")