cat1 = int(input("Ingrese el primer cateto : "))
cat2 = int(input("Ingrese el segundo cateto : "))

hip = pow(pow(cat1,2) + pow(cat2,2),1/2)
hip = round(hip,(2))

mayor = max(cat1, cat2)
menor = min(cat1, cat2)

print("The hypotenous of this triangle is ", hip)
print("The bigger catet is ", mayor)
print("And the little one is ", menor)

