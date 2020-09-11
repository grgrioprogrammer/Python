#Desarrolle un programa completo en Python, sin usar las funciones predefinidas min() y max(),
#que permita ingresar tres números (suponga que son todos distintos)
#y muestre el  mayor y el menor. Luego informe por pantalla si el mayor es divisible por
#(o es múltiplo de) el menor.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 > num2 and num1 > num3:
    mayor = num1
    if num2 > num3:
        medio = num2
        menor = num3
    else:
        medio = num3
        menor = num2
elif num2 > num3 and num2 > num3:
    mayor = num2
    if num3 > num1:
        medio = num3
        menor = num1
    else:
        medio = num1
        menor = num3
elif num3 > num2 and num3 > num1:
    mayor = num3
    if num2 > num1:
        medio = num2
        menor = num1
    else:
        medio = num1
        menor = num2

print("El mayor de los numeros ingresados es el",mayor,"y el menor es el ", menor,".")

if mayor % menor == 0:
    print("Es divisible.")
else:
    print("No es divisible.")

