segundos = int(input("Ingresar cantidad de segundos a convertir: "))

minutos = segundos // 60
segundos_resto = segundos % 60

horas = minutos // 60
minutos_resto = minutos % 60

print("Horas",horas,"Minutos",minutos_resto,"Segundos",segundos_resto)



