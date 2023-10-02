# for numero in range(5):
#     print("numero: ", numero * 'hola mundo')


buscar = 10
for numero in range(5):
    print(numero)
    if buscar == numero +1 :
        print('encontrado el elemento', buscar, " en la posicion", (numero+2))
       # break
else:
    print ("el valor no se encuentra")
        
        
# for char in "Ultimate Python":
#     print(char.upper())