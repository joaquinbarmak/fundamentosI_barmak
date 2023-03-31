import os

# Ingresar los nombres de los archivos acá
file1 = "hola.txt"
file2 = "chau.txt"

os.rename(file1, "temp")
os.rename(file2, file1)
os.rename("temp", file2)
 # tarea: modificar el script para que tome el nombre de los archivos desde la terminal
 # posiblemente haya que incluir os.path.exists(path)