class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Pato(Caminador, Volador, Nadador):
    def programar(self):
        print("programando")


# Instancia de la clase Pato
pato = Pato()

# Llamadas a los métodos de las clases base
pato.caminar()
pato.volar()
pato.nadar()
pato.programar()
