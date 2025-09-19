#IF- SINTAXIS
""""
if condicion : #puede ser TRUE/FALSE 
  #Codigo que se ejecuta si la condicion es TRUE
   print("instruccion 1")
   print("instruccion 2")
   print("instruccion 3")
else:   
    print("instruccion A")
    print("instruccion B")
    print("instruccion C")
""" 
tiene_carnet =False


if tiene_carnet:
    print("puede ingresas a la biblioteca")
    print("Bienvenido")
else:
    print("No tienes acceso")
    print("te recomendamos hacerte socio")
    


libros_prestado=int(input("Ingrese cantidad de lirbos prestados: "))
if libros_prestado < 3:
    print("puedes pedir un nuevo libro")           
else:
    print("Haz alcanzado el limite de libros prestados")
print("Muchas gracias por visitar la biblioteca de Tech")