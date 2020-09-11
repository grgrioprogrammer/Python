print('Conversion de distancias')
pies = float(input('Ingrese la distancia en pies que desea convertir: '))

# Procesos
yardas = round(pies / 3, 2)
pulgadas = round(pies * 12, 2)
centimetros = round(pulgadas * 2.54, 2)
metros = round(centimetros / 100, 2)

# Presentacion de resultados
print('En', pies, 'pies hay', yardas, 'yardas')
print('En', pies, 'pies hay', pulgadas, 'pulgadas')
print('En', pies, 'pies hay', centimetros, 'centimetros')
print('En', pies, 'pies hay', metros, 'metros')
