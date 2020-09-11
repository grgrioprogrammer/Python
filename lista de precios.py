G = 6.673 * 10 ** -8
m1 = int(input("Ingrese la masa del primer cuerpo : "))
m2 = int(input("Ingrese la masa del segundo cuerpo : "))
d = int(input("Ingrese la distancia entre los cuerpos : "))
f = G * (m1 * m2 / d ** 2)
print("La intensidad de la fuerza es de", f)
