if __name__ != "__main__":
    from ..gestion.crud import guardar

    print(__name__)

    def pagar_impuesto():
        print("pagando impuesto")
        guardar()

if __name__ == "__main__":
    print("tarea de mantenimiento")
