tiene_carnet = True
libro_debe = 0

# AND
puede_pedir= tiene_carnet == True and libro_debe ==0
print("puede pedir un libro ? :" , puede_pedir )


#OR


es_bibliotecario =False
es_administrador=True

puede_modificar_registros = es_bibliotecario == True or es_administrador == True
print("puede modificar registros en el sistema?:" , puede_modificar_registros)


#negacion o NOT 

tiene_multa = False
puede_renovar_libros = not tiene_multa

print ("Puede renovar su prestamo ?" , puede_renovar_libros)
