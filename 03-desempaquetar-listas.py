numeros = [1, 2, 3, 4, 5]

# feo
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[3]
# cuarto = numeros[4]

primero, segundo, *otros, ultimo = numeros
print(primero, segundo, ultimo)