numero = int(input("numero 1: "))

unidad = numero % 10
decena = numero % 100
centena = numero % 1000
print('El ultimo digito del numero', numero, 'es', unidad)
print('Los ultimos 2 digitos del numero', numero, 'son', decena)
print('Los ultimos 3 digitps del numero', numero,'son', centena)
