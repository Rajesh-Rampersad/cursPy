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