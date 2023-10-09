punto = {"x": 20, "y":"40"}

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)
if "lalla" in punto:
    print(punto["lalla"])
    
print(punto.get("lala", 50))
print(punto.get("x"))
#del punto["z"]
#del (punto["y"])

# for valor in punto:
#     print(valor, punto[valor])

for valor in punto.items():
    print(valor)
    
for llave, valor in punto.items():
    print(llave, valor)
    
usuarios = [
    {"id": 1, "nombre": "pedro"},
    {"id": 2, "nombre": "jose"},
    {"id": 3, "nombre": "carlos"},
    {"id": 4, "nombre": "felipe"}
]

for usuario in usuarios:
    print(usuario["id"])