"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    # Paso 1: Validar argumentos
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    # Paso 2: Obtener ruta del archivo
    file_path = sys.argv[1]

    # Paso 3: Mostrar argumentos
    print("Command-line arguments:")
    for arg in sys.argv[1:]:
        print(arg)

    # Paso 4: Leer tareas
    tasks = read_todo_file(file_path)

    # Paso 5: Mostrar tareas
    print("\nTasks:")
    for task in tasks:
        print(task)

except IndexError as e:
    print(e)