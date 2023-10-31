class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    @classmethod
    def habla(cls):
        print(" Gua!")
        
    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 4)
        
Perro.habla()
perro1 = Perro("Chanchito", 1)
perro2 = Perro("Carlos", 2)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)