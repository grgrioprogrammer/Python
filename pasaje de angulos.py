angulo_en_segundos = int(input("Ingrese sus segundos a convertir : "))

grados = angulo_en_segundos // 3600
resto_grados = angulo_en_segundos % 3600
minutos = resto_grados // 60
segundos = resto_grados % 60


print("Angulo en sexagecimal", grados, "°", minutos, "'", segundos, '"')

