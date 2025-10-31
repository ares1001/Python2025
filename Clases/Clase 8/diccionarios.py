"""
Diccionarios en Python
Estructurar nuestros datos por medio de elementos que contengan
pares key- values
Pequeños contenedores organizados , desordenados , mutabñes , las key son unicas
SINTAXIS 
"ket": "value"

"""


person = {
    "first_name" : "Ariel", 
    "last_name" :"Rodriguez",
    "email" :"ari@gmail.com",
    "age": 33,
    "DNI":25355556,
    "is_student" :False,
    "address": {"calle" : "Thames", 
                "altura" :500, 
                "ciudad" :"Caba"}


}

inventory = {
    "arroz" : 50,
    "azucar" : None,
    "manteca" :10,
    "harina" : 10
}

print(inventory)


"""
FUNCIONES BASICAS CON NUESTRO DICCIONARIO
"""
#si necesito acceder a un valor lo voy a hacer por medio de la key
print(f"Cantidad de arroz : {inventory['azucar']}")


#Existe una funcion .get() para tener el valor de una key
#si no existe devuelve None po un valor por defecto que se le indique

print(f"Cantidad de manteca : {inventory.get('manteca')}")


#Agregar elementos key- values 
inventory['Leche'] = 100
inventory['vino'] = 50
print(inventory)


#Modificar elementos
inventory["arroz"] = 100
print(inventory)

#elimimar elementos
del inventory["azucar"]
print(inventory)
#podemos eliminar con la funcion pop(),permite extraer el valor y luego elimina la key

manteca = inventory.pop("manteca")
print(f"cantidad de manteca : {manteca}")
print(inventory)

#obtencion  keys()
inventory_keys = inventory.keys()
print(inventory_keys)
for key in inventory_keys:
    print(f"Clave : {key}")



#recorremos values ()

inventory_values = inventory.values()
print(inventory_values)
for value in inventory_values:
    print(f"valor : {value}")


#recorremos pares ()

pairs = inventory.items()
print(pairs)
for key , value in pairs:
    print(f"key : {key} - Value : {value}")

