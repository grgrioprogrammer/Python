#Debo presentar el nombre completo de los pospulantes de una vecindad
#ademas debo mostrar tantas "x" como votos obtenidos por cada postulante

nombre = input("Nombre del postulante: ")
apellido = input("Apellido del postulante: ")
votos = int(input("Cantidad de votos: "))
cantidad_x = ('x' * votos)
print('(',votos,')')
print(nombre[0] + apellido[0])
print(cantidad_x)




