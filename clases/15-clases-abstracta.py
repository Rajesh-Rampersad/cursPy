
from abc import ABC, abstractclassmethod


class Model():
    @property
    @abstractclassmethod
    def tabla(self):
        pass

    @abstractclassmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, id):
        print(f"Buscando por id {id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
