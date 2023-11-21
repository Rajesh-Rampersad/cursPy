class Perro:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __del__ (self):#destructor
        print(f"Chao perro 🥺 {self.nombre}")
        
    def habla(self):
        print(f"{self.nombre} dice: Gua!")
        
    def __str__(self) -> str:
        return f"Clase Perro: {self.nombre}"
        

perro = Perro("Chanchito",1)

del perro