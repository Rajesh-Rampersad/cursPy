print("Bienvenido a la calculador")
print("Para salir, escribe salir")
print("las opereciones permitida son suma, resta, multiplicar y division")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa la operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa el siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    
    if op.lower() == "suma":
       resultado += n2
       
    elif op.lower() == "resta":
       resultado -= n2
       
    elif op.lower() == "multi":
       resultado *= n2
       
    elif op.lower() == "div":
       resultado /= n2
       
    else:
        print(" Operacion no valida")
        break
    print(f"El resultado es {resultado}")
    