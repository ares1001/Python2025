#reto 3: Validación de formato de número telefónico,
#Un sistema de contacto necesita asegurarse de que los teléfonos sean de formato nacional.
# Por lo que se debe solicitar al usuario el ingreso de número y 
# se debe verificar que empiece con "+54" 
#y que contenga 13 caracteres.



# telefono =(input("Ingrese su numero telefonico indicando tambien el codigo del pais , ej  +54 "))
# longitud =len(telefono)

# if telefono.startswith("+54") and longitud ==13:
#     print("el telefono ingresado es correcto")
# else:
#     print("el numero ingresado tiene un formato incorrecto")


# if not telefono.startswith("+54"):
#     print("numero ingresado debe iniciar con +54")
# elif len(telefono) !=13:
#     print("la extension del numero debe ser de 13 caracteres")
# else:
#     print("numero ingresado correctamente")

# tel=input("ingresa tu numero de telefono (ej + 5491126632312: ")
# while not tel.startswith("+54") and len(tel) !=14:
#     print("el numero ingresado es erroneo")
#     tel = input("ingreso tu numerp celular(ej. +5491126632312)")
# else: #se eejcuta cuando la condicion del while es falsa
#     print("el numero es correcto")

#siempre lleva break porque hasta que no se rompe el true , no para 

while True: 
    tel = input("ingresa tu numero de telefono (ej + 5491126632312: ")
    if not tel.startswith("+54") or len(tel) !=14:
        print("el numero ingresado es erroneo.Intente nuevamente")
        continue
    else:
         print("el numero es correcto")
         break
    

    #Listas


