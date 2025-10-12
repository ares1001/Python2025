"""
Manejar una lista 
Bicis , modelo , precio
# Pre entrega lab - Requisitos

## Check list acciones

* **Ingreso de datos de productos:**
El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos). Estos datos deben almacenarse en una lista, donde cada cliente sea representado/a como una sublista de tres elementos (nombre, categoría, y precio).
* **Visualización de productos registrados:**
El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos ingresados. La información debe presentarse de manera ordenada y legible, con cada producto numerado.
* **Búsqueda de productos:**
El sistema debe permitir buscar productos por su nombre. Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan. Si no hay coincidencias, debe informar que no se encontraron resultados.
* **Eliminación de productos:**
El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista.

## Check list técnico

*   Usar listas para almacenar y gestionar los datos. (Lista de listas)
*   Incorporar bucles while y for según corresponda.
*   Validar entradas del usuario
*   Utilizar condicionales para gestionar las opciones del menú
*   Presentar un menú que permita elegir entre las funcionalidades disponibles.
*   El programa debe continuar funcionando hasta que se elija una opción para salir.

## MANOS A LA OBRA



"""


bike_1= ["Canyon", "Speedmax",5500]
bike_2=["Cervelo", "P5", 8600]
bike_3 =["Specialized", "Shiv", 6300]
bike_4=["Felt" , "B12", 1800]


bikes=[bike_1, bike_2,bike_3,bike_4 ]






menu = """
    ***** Menu *****
    1. Agregar un bicicleta a nuestro catalogo
    2. Mostrar todos los bicicletas de Lebron Bike Shop
    3. Buscar un bicicleta en nuestro E-Shop
    4. Eliminar un bicicleta del E-Shp
    5. Salir
  
"""


#Algoritmo 

print ("**********Bienvenidos Lebron Bike Shop***********")
while True:
    print(menu)
    option = input("\nSeleccione la opcion deseada(1-5) :")
    match option:
        case "1":
            #agregamos el producto
            print("\nIngrese los datos de la bicicleta que sea agregar :")
            brand = input("Marca :").strip()
            #validar 
            while not brand :
                print("Tiene que agregar una marca")
                brand = input("Marca : ").strip()

            model = input("Modelo:").strip()
            price = int(input("Precio :"))

            #Creo el nuevo modelo
            new_bike =[brand, model, price]

            #lo agrego al final de la lista
            bikes.append(new_bike)
            print(f"La bicicleta {brand}, {model} fue agregada a nuestro E-Shop")
            input(" \nPresione Enter para volver al menu") 
        case "2":
            #aca mostramos todas las bicieltas 
            print(f"\nbicicletas disponibles {len(bikes) :}")
            for index in range(len(bikes)):
                print(f"{index+1} - Marca : {bikes[index][0]}  Modelo : {bikes[index][1]}  Precio: {bikes[index][2]}")
            input(" \nPresione Enter para volver al menu") 

        case "3":
            print("\n******Busca en nuestro E-Shop tu proxima bicicleta******".upper()
                  )
            search_bike = input("Ingresa la marca que esta buscando : ").strip()

            for bike in bikes :
                # no impoprta si escribe en mayusculas o minisculas
                if bike[0].lower() == search_bike.lower():
                    print(f"\nBicicleta encontrada : Marca :{bike[0]} ,Modelo : {bike[1]} ,Precio : {bike[2]} ")
                    break
            else:
        # Este else se ejecuta si el for terminó sin encontrar nada
                 print("\nNo se encontró ninguna bicicleta con esa marca.")

            input("\nPresione Enter para volver al menú")
              
        case "4":
       
            # print("has seleccionado la opcion Eliminar bicicleta")  
            if not bikes :
                print("No hay bicicletas para eliminar")
                input(" \nPresione Enter para volver al menu")
                continue

            print("\n********Estas a punto de eliminar una bicicleta*********".upper())

            for index , bike in enumerate(bikes) :
                print(f"{index} - Marca : {bike[0]} Modelo : {bike[1]}")
               
                #Solcitar al usuario la posicion
            posicion=int(input("Ingrese el numero de bicicleta que desea eliminar: "))
            #validar el indice
            if 0<= posicion < len(bikes):
                del_bike = bikes.pop(posicion)

        
                print(f"La bicicleta {del_bike[0]} {del_bike[1]} ha sido eliminada")
            else :
                print(f"has ingresado un numero invalido")
            # for i in range(len(bikes)):
            #     print (f" {i+1} Marca : {bikes[i][0]} Modelo : {bikes[i][1]} Precio ${bikes[i][2]}")

            # del_bike = int (input("Ingrese el numero de la bicicleta que desea eliminar :"))

            # del_bike_index = del_bike -1
            
            # if 0 <= del_bike_index < len(bikes):
            #  deleted = bikes.pop(del_bike_index)
            #  print(f"Bicicleta {deleted[0]} {deleted[1]} eliminada correctamente")
            # else:
            #     print("indice invalido, no existe es bicicleta")
            
            input(" \nPresione Enter para volver al menu") 


             
            #Mostras todas las bicicletas
            #pedirle al usuario el indice
            # chequar el valor
            # Eliminar
        
          
            # del bikes[0]
            # print(bikes)
            # print(len(bikes))
             
        case "5":
            #Salir
            # print("\nSalir de nuestro E-Shop")
            break
        case _: # si ingresa cualquier numero
            print("\n Opcion invalida, intente nuevamente")
            input(" \n Presione Enter para volver al menu")

print("\n********Gracias por ser parte de Lebron Bike Shop************")

       