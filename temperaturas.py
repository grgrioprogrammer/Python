temp_1 = int(input("primera temperatura: "))
temp_2 = int(input("segunda temperatura: "))
temp_3 = int(input("tercera temperatura: "))
temp_4 = int(input("cuarta temperatura: "))

promedio_temp = (temp_1 + temp_2 + temp_3 + temp_4) / 4

print("El promedio de las temperaturas es de", promedio_temp, "grados centigrados.")

if temp_1>temp_2 and temp_1>temp_3 and temp_1>temp_4:
    maxima = temp_1

if temp_2>temp_1 and temp_2>temp_3 and temp_2>temp_4:
    maxima = temp_2

if temp_3>temp_2 and temp_3>temp_1 and temp_3>temp_4:
    maxima = temp_3

if temp_4>temp_2 and temp_4>temp_3 and temp_4>temp_1:
    maxima = temp_4

print("La maxima temperatura registrada es de ", maxima, " grados centigrados.")

if temp_1<temp_2 and temp_1<temp_3 and temp_1<temp_4:
    minima = temp_1

if temp_2<temp_1 and temp_2<temp_3 and temp_2<temp_4:
    minima = temp_2

if temp_3<temp_2 and temp_3<temp_1 and temp_3<temp_4:
    minima = temp_3

if temp_4<temp_2 and temp_4<temp_3 and temp_4<temp_1:
    minima = temp_4

print("La minima temperatura registrada es de", minima, "grados centigrados.")

supera_promedio = False
if temp_1 > promedio_temp or temp_2 > promedio_temp or temp_3 > promedio_temp or temp_4 > promedio_temp:
    supera_promedio = True

if supera_promedio:
    print("Una de las temperaturas supera el promedio")

