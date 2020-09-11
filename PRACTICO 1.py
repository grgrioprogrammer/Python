print("Este programa fue diseñado para que las respuestas de carga sean con 'si' o 'no' y numeros cuando lo pida,\nla "
      "temperatura puede"
      " ser cargada de manera decimal, la edad debe ingresarse de manera entera.")

#Datos
si = str("si")
neu = input("¿Padece o padecio neumonía? (si o no): ")
if neu == si:
    print("Caso sospechoso")
    exit()

if neu != si:
    edad = int(input("Ingrese la edad: "))

    if neu != si:
        temp = float(input("Ingrese temperatura corporal (ej: 36.5): "))

        if temp > 37.5:
            sintomas = tuple(input("Ingrese sintomas (ej: tos, edinofagia, problemas respiratorios, etc): "))


contact = input("¿Estuvo en contacto con casos sospechosos? (si o no): ")

if contact != si:
    viajo_int = input("¿Há visitado zonas locales de contagio registradas? (si o no): ")

    if viajo_int != si:
        viajo_ext = input("¿Viajo al exterior en los últimos 14 dias? (si o no): ")

        if viajo_ext != si:
            psalud = str(input("¿Es personal de salud? ( si o no): "))

#Procesos

if neu != si and (temp > 37.5 or edad >= 60 and len(sintomas) >= 1):
    print("Presenta Caso Sospechoso")

elif edad >= 60 and neu != si and temp <= 37:
    print("No es caso sopechoso pero esta en riesgo")

if temp > 37.5:
    print("Presenta Fiebre")

    if contact == si:
        print("Estuvo en Contacto con un Caso Sospechoso")

    if viajo_int == si:
        print("Pudo contagiarce en ciudades de riesgo")

    elif viajo_ext == si:
        print("Pudo contagiarce en ciudades extranjeras de riesgo")

    elif psalud == si:
        print("Pudo contagiarce en un centro de salud")
    else:
        print("Caso No Sospechoso")
