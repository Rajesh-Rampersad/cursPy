try:
    n1 = int(input("Ingresa primer número: "))
except Exception as e:
    print("Ocurrio un error, solo se permite números")

else:
    print("No ocurrio ningun error")
finally:
    print("Se ejecuta siempre")
