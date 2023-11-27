class Model():
    tabla = False

    def __init__(self) -> None:
        if not self.tabla:
            print("Error,tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, id):
        print(f"Buscando por id {id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
