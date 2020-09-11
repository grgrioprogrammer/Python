pc_1 = int(input("Numero de serie de PC-1: "))
tiempo_reparacion_pc_1 = int(input("Duracion de la reparacióm: "))
problema = input("a. Problema de Software - b. Problema de Hardware: ")

if problema == "a":
    print("El equipo PC-1 tiene un problema de Software.")
else:
    print("El equipo PC-1 tiene un problema de Hardware.")

pc_2 = int(input("Numero de serie de PC-2: "))
tiempo_reparacion_pc_2 = int(input("Duracion de la reparacióm: "))
problema = input("a. Problema de Software - b. Problema de Hardware: ")
if problema == "a":
    print("El equipo PC-2 tiene un problema de Software.")
else:
    print("El equipo PC-2 tiene un problema de Hardware.")

pc_3 = int(input("Numero de serie de PC-3: "))
tiempo_reparacion_pc_3 = int(input("Duracion de la reparacióm: "))
problema = input("a. Problema de Software - b. Problema de Hardware: ")
if problema == "a":
    print("El equipo PC-3 tiene un problema de Software.")
else:
    print("El equipo PC-3 tiene un problema de Hardware.")


tiempo_total = (tiempo_reparacion_pc_1 + tiempo_reparacion_pc_2 + tiempo_reparacion_pc_2)

print("El tiempo total es de",tiempo_total, "minutos.")


if tiempo_reparacion_pc_1 > tiempo_reparacion_pc_2 and tiempo_reparacion_pc_1 > tiempo_reparacion_pc_3:
    print("El equipo que mas tiempo necesito para ser repadado es el PC-1.")

elif tiempo_reparacion_pc_2 > tiempo_reparacion_pc_3:
    print("El equipo que mas tiempo necesito para ser reparado es el PC-2.")

else:
    print("El equipo que mas tiempo necesito para ser reparado es el PC-3.")

