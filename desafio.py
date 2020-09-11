segundos = int(input("Ingrese la cantidad de segundos que desee : "))

minutos = segundos // 60
segundos_resto = segundos % 60
horas = minutos // 60
minutos_resto = minutos % 60

print(horas, minutos_resto, segundos_resto)



