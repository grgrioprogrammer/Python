km = int(input("Cuantos kilometros recorrio: "))
tarifa = 500
exedente = 3 * (km - 300)
exedente2 = 1.5 * (km - 300)
if km < 300:
    print("Se le cobraran",tarifa)
elif 300 <= km <= 1000:
    print("Se le cobraran", tarifa + exedente)
elif km > 1000:
    print("Se le cobrara", tarifa + exedente2)




