# numeros = [1, 2, 3, 4]
# # print(1, 2, 3, 4)
# # print(*numeros)

# numeros2 = [5,6, 7]

# combinada = ["hola",*numeros, "que tal", *numeros2]
# print(combinada)

#prueba con diccionario

punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2, "z":"mundo"}
print(nuevoPunto)