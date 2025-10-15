"""
LISTAS 
son como los array
"""
from colorama import Fore, Back, Style, init

numbers =[43,56,100,56,299] # Lista vacia 
print(type(numbers))
print(numbers)


names = ['Caro', 'Ariel', 'Milo']


# elementos hetergoneos

product_1= ['Galletas' , 10, 1399.99, 'Oreo']
product_2= ['Arroz' , 30, 399.99, 'Matarazzo']
product_3= ['Leche' , 20, 2399.99, 'La Serenisima']


#lista de listas

products = [product_1, product_2, product_3]
print(products)




#Acciones con listas

books = ['Principito', 'Rayuela', 'El señor de los anilllos', 'el quijote']

print(books[0 *1])
print(f'cantidad de elementos :{len(books)}')


#modificar un elemento por su posicion 

books[3]='El Quijote de la mancha'
print(books)


#agregar elementos al final 
books.append("Harry Potter")
print(books)
print(len(books))


#eliminar elementos de la lista
# del books[0]
# print(books)
# print(len(books))

#eliminar por valor
# books.remove("Rayuela")
# print(books)
# print(len(books))


#Obtener indice
index = books.index("Rayuela")
print(f"Rayuela en la posicion: {index}")



#listas de correos 
email_domains =["gmail.com" , "hotmail.com" , "yahoo.com"]
email= input("ingrese su email : ")
for domain in email_domains:
    if domain in email:
        print("el email contiene un dominio valido")
        break
else:
    print(" no contiene un dominio valido")

