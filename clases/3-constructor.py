class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    def habla(self):
        print("Gua!")
        
mi_perro = Perro("Chanchito")
print(mi_perro.nombre)