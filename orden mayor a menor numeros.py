a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))


if a>b and a>c:
     may=a
     if b>c:
         med=b
         men=c
     else:
         med=c
         men=b
elif b>c and b>a:
     may=b
     if c>a:
         med=c
         men=a
     else:
         med=a
         men=c
else:
     may=c
     if b>a:
         med=b
         men=a
     else:
         med=a
         men=b

print(may, med, men)

if men==may%med:
     print("El tercero es igual al resto de la división de los dos primeros")
else:
     print("El tercero NO es igual al resto de la división de los dos primeros")
