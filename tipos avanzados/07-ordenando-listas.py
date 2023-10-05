numeros = [20, 4, 6, 18, 104, 120, 114, 216]

#numeros.sort(reverse=True)
numeros2 =sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

ususarios = [["carlos", 4],
             ["ana", 1],
             ["Felipe", 5]
             ]

def ordenar(elemento):
    return elemento[1]

ususarios.sort(key=ordenar, reverse=True)
print(ususarios)