grados = int(input("ingrese los grados del angulo : "))
minutos = int(input("ingrese los minutos del angulo : "))
segundos = int(input("ingrese los segundos del angulo : "))



minutos_en_grados = minutos / 60
segundos_en_grados = segundos / 3600
angulo_en_grados = grados + minutos_en_grados + segundos_en_grados

print("Angulo en grados", angulo_en_grados,"°",)

grados_en_minutos = grados * 60
segundos_en_minutos = segundos / 60
angulo_en_minutos = grados_en_minutos + minutos + segundos_en_minutos

print("Angulo en minutos", angulo_en_minutos,"'")

grados_en_segundos = grados * 3600
minutos_en_segundos = minutos * 60
angulo_en_segundos = grados_en_segundos + minutos_en_segundos + segundos

print("Angulo en segundos", angulo_en_segundos, '"')



#debemos realizar un programa que nos muestre un angulo sexagecimal, solo en grados, solo minutos y solo segundos.
