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

from colorama import Fore, Back, Style, init
 
init()


# bike_1= ["Canyon", "Speedmax",5500]
# bike_2=["Cervelo", "P5", 8600]
# bike_3 =["Specialized", "Shiv", 6300]
# bike_4=["Felt" , "B12", 1800]


# bikes=[bike_1, bike_2,bike_3,bike_4 ]

bike_1 = {'marca' : "Canyon",
          "modelo" :"Speedmax",
         "precio":6500
          }

bike_2= {'marca' : "Cervelo",
          "modelo" :"P5",
          
           "precio":5500
          }

bike_3= {'marca' : "Specializez",
          "modelo" :"Shiv",
        "precio":3500
          }


bike_4= {'marca' : "Felt",
          "modelo" :"B12",
          "precio":2500
          }

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
print("                                                   ")
print("                                                   ")
print (Fore.RED  + "**********Bienvenidos Lebron Bike Shop***********")
while True:
    print(menu)
    option = input("\nSeleccione la opcion deseada(1-5) :")
    match option:
        
        case "1":
            #agregamos el producto
            print("\nIngrese los datos de la bicicleta que sea agregar :")
            brand = input("Marca: ").strip()
            #validar 
            while not brand :
                print(Fore.RED  +"Tiene que agregar una marca")
                brand = input("Marca: ").strip()

            model = input("Modelo: ").strip()
            
            
            #Validacion de precio 
            price = int(input("Precio: "))
            while price <=0 :
                print( " el precio tiene que ser mayor a 0 ")
           
                price=int(input("Precio:  "))
            
           

            new_bike ={"marca" : brand,
                       "modelo": model,
                       "precio": price}

            #lo agrego al final de la lista
            bikes.append(new_bike)
            print(f"La bicicleta {brand}, {model} fue agregada a nuestro E-Shop")
            
            #Volver al menu principal o salir 
            option = input("\nPresione Enter para volver al menu anterior o escriba '5' para salir ").strip()            
            if option =="5":
                print(Fore.GREEN+ "\nGracias por ser parte de la fanilia Lebron Bike Shop")
                break
        case "2":
            #aca mostramos todas las bicicletas 
            if len(bikes) > 0 :


                for bike in bikes :
                    print(f"- marca: {bike['marca']} modelo: {bike['modelo']} precio: {bike['precio']}")
            else:
                print(Fore.YELLOW+'No hay bicicletas en stock')
                break
            
            
            if option =="5":
                print("\nGracias por ser parte de la fanilia Lebron Bike Shop")
                break
        case "3":
            
            if len(bikes) > 0:
                print("\n******Busca en nuestro E-Shop tu proxima bicicleta******".upper())
            search_bike = input("Ingresa la marca que esta buscando : ").strip()

            for bike in bikes :
                # no impoprta si escribe en mayusculas o minisculas
                if bike['marca'].lower() == search_bike.lower():
                    print(f"\nBicicleta encontrada : Marca :{bike['marca']} ,Modelo : {bike['modelo']} ,Precio : {bike['precio']} ")
                    break
            else:
        # Este else se ejecuta si el for terminó sin encontrar nada
                 print("\nNo se encontró ninguna bicicleta con esa marca.")
            
            option = input("\nPresione Enter para volver al menu anterior o escriba '5' para salir ").strip()            
            if option =="5":
                print("\nGracias por ser parte de la fanilia Lebron Bike Shop")
                break  
        case "4":
            

            # has seleccionado la opcion Eliminar bicicleta
            if not bikes:
                print("No hay bicicletas para eliminar")
                input("\nPresione Enter para volver al menú")
                continue

            print("\n******** ESTÁS A PUNTO DE ELIMINAR UNA BICICLETA *********".upper())

            for index, bike in enumerate(bikes):
                print(f"{index} - Marca: {bike['marca']} Modelo: {bike['modelo']}")

            # 🔁 Repetir hasta que ingrese un número válido
            while True:
                posicion = int(input("\nIngrese el número de bicicleta que desea eliminar: "))

                if 0 <= posicion < len(bikes):
                    del_bike = bikes.pop(posicion)
                    print(f"La bicicleta {del_bike['marca']} {del_bike['modelo']} ha sido eliminada.")
                    break  # Sale del while si se eliminó correctamente
                else:
                    print("Número inválido. Intente nuevamente.")

            option = input("\nPresione Enter para volver al menú anterior o escriba '5' para salir ").strip()
            if option == "5":
                print(Fore.GREEN + "\nGracias por ser parte de la familia Lebron Bike Shop")
                break

        
    
             
        case "5":
            #Salir
           
            break
        case _: # si ingresa cualquier numero
            print("\n Opcion invalida, intente nuevamente")
            input(" \n Presione Enter para volver al menu")

print(Fore.GREEN+"\n********Gracias por ser parte de Lebron Bike Shop************")

       