"""
MATCH
sintaxis basica 

match variable : 
    case valor1:
        #codigo si cumple el valor 1
    case valor2
        #codigo si cumple el valor 2
    case valor3
        #codigo si cumple el valor 3
    case_:
    # caso por defecto( no cumnple con las anteriores)
"""

#situacion de un menu de opciones
# 1 , crear libro 
# 2 , mostar libro
# 3, Modificar libro
# 4, eliminar libro
# 5 salir del sistema
# print("##### MENU #####")
# print("1. Crear Libro")
# print("2. Mostrar Libro")
# print("3. Modificar Libro")
# print("4. Eliminar Libro")
# print("5. Salir del sistema")

# opcion =int(input("seleccione la opcion deseada: "))
# match opcion:
#     case 1:
#         print("Ingrese a la accion de crear libro")
#     case 2:
#         print("Mostrando libros")
#     case 3:
#         print("Modificar libro")
#     case 4:
#         print("Eliminar libro")
#     case 5:
#         print("Graciass por usar el sistema")
#     case _:
#         print("opcion incorrecta")

dias_retraso = 5
match dias_retraso:

    case 0:
        print("Sin retraso")
    case 1 | 2:
        print("Multa leve")
    case 3 |4 |5 :
        print("Multa media")
    case 6 | 7| 8:
        print("Multa grave")
    case _:
        print("Valor mal ingresado ")