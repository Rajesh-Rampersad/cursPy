from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependecias = {
    "db": "base de datos",
    "api": "esta es una api",
    "graphql": "esto es graphql"
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependecias)
    except:
        print("El paquete no tiene funcion init")


list(map(load, paths))
