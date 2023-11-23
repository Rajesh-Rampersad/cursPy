from pathlib import Path

path = Path("rutas")
# path.exists() #verificar si existe
# path.mkdir() #crear un directorio
# path.rmdir() #remover  directorio
# path.rename() # para renombrar directorio
# for p in path.iterdir():
#     print(p)

# archivos = [p for p in path.iterdir() if not p.is_dir()]
# archivos = [p for p in path.glob("01-*.py")]
archivos = [p for p in path.glob("**/*.py")]
print(archivos)
