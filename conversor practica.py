horas = int(input("Ingrese horas : "))
minutos = int(input("Ingrese minutos : "))
segundos = int(input("Ingrese segundos : "))

segundos_1 = horas * 3600
segundos_2 = minutos * 60
segundos_3 = segundos

total = segundos_1 + segundos_2 + segundos_3
print("El total de segundos es de", total,)
