#reto 3: Validación de formato de número telefónico,
#Un sistema de contacto necesita asegurarse de que los teléfonos sean de formato nacional.
# Por lo que se debe solicitar al usuario el ingreso de número y 
# se debe verificar que empiece con "+54" 
#y que contenga 13 caracteres.



telefono =(input("Ingrese su numero telefonico indicando tambien el codigo del pais , ej  +54 "))


if telefono.startswith("+54"):
    print("el telefono ingresado es correcto")
else:
    print("el numero ingresa tiene un formato incorrecto")