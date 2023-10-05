# set significa grupo o conjunto

primer = {1, 1, 2, 2, 3, 3, 4}
segundo = [3, 4, 5, 6]
tercero =set(segundo)

#union
#print(primer | tercero)

#interseccion
#print(primer & tercero)

#diferencia
print(primer - tercero)

#diferencia simetrica
print(primer ^ tercero)

if 5 in segundo:
    print("prueba superada")