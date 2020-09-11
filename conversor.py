horas = int(input("Ingrese horas : "))
minutos = int(input("Ingrese minutos : "))
segundos = int(input("Ingrese segundos : "))

horas_a_segundos = horas // 3600
minutos_a_segundos = minutos // 60
resto_segundos = segundos % 60

total = horas_a_segundos + minutos_a_segundos + resto_segundos

print(total)




