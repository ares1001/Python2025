"""Slicing"""
texto = "Python es divertido"

#slicing basico
print(texto[0:8]) #posicion inicial y posicion final que no lo incluye


#si necesitamos partir desde el inicio 
print(texto[:4]) #desde el inicio hasta el numero que le indique


print(texto[7:]) # desde donde le indico hasta el final

print(texto[:])

#subcadena con paso
copy_text = texto[10::2] # con un tercer parametro indico los saltos entre el intervalo
print(copy_text)
print(texto[-9:])

path_file= 'archivo.pdf'
print(path_file[0:-4])


"""
f-string: es una forma de formatear cadenas
"""

nombre= "Caro"
print(f"Hola,{nombre}")


cantidad_libros = 10 
print(f"{nombre} ha solicitado {cantidad_libros +10 } libros")


multa = 4.54575852655
print(f" la multa total es de ${multa:.4f}")


"""
WHILE # Estructuras repetitivas - WHILE
WHILE
Nos permite repetir un bloque de codigo mientras una condición se cumple
La condicion a evaluar y asegurarnos que esa condición en algun punto se
vuelva falsa.
Sintaxis basíca:

while condicion: #mientras la condición sea verdadera
    #Instruccion 1
    #Instruccion 2
    #Instruccion 3
    #Instruccion 4

"""

# correct_password = "python123"
# entered_password = input("Ingrese su contraseña: ")

# while correct_password != entered_password:
#     print("Acceso denegado, usuario o contraseña incorrecta")
#     entered_password = input("Ingrese su contraña, nuevamente: ")

# print("Acceso correcto, puede ingresar al sistema")


#INICIALIZACION
coins = 0

while coins < 5:
    print(f"Tienes {coins} monedas.")
    #Incremento una moneda
    coins = coins + 1  # coins += 1

print("Recolectaste 5 monedas, tienes una vida más")


#CUENTA REGRESIVA
countdown = 5

while countdown > 0:
    print(f"Despegue en {countdown}...")
    countdown = countdown - 1 # countdown -= 1

print("Despegando 🚀")

"""
ACUMULADORES
usamos para almacenar valores que pueden ir incrementando o decreciendo de forma arbritraria
Su uso frecuente-> sumar valores, acumular resultados, concatenar cadenas
Inicializar por fuera del bucle
Actualizar su valor dentro del bucle
Una vez finalizado el bucle tendremos el valor final del acumulador
"""

#INICIALIZAMOS
# day_counter = 0 # <- el contador de dias
# temperature_sum = 0 #<- el acumulador de temperaturas

# while day_counter < 7:
#     temperature = float(input(f"Ingrese la temperatura (ºC) del dia {day_counter + 1}: "))
#     temperature_sum = temperature_sum + temperature #temperature_sum += temperature
#     day_counter += 1 #Incremento el valor de los dias

# #calcular el promedio
# average = temperature_sum / day_counter
# print(f"El promedio de temperaturas de la semana es: {average:.2f} ºC")



"""
BREAK y CONTINUE
"""

total_expenses = 0

while True:
    expense = float(input("Ingresa el gasto (0 para finalizar): "))
    if expense == 0:
        break # fuerza la salida del bucle, si el gasto es 0
    elif expense < 0:
        print("No se permite gastos menores a 0.")
        continue #Saltearme a la siguiente iteracion

    total_expenses += expense

print(f"Gastos totales del día:$ {total_expenses:.2f}")
