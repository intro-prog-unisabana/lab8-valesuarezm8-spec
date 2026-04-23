"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
import sys

try:
    
    total_load = float(sys.argv[1])
    num_supports = float(sys.argv[2])

    # Paso 2: Validar división por cero
    if num_supports == 0:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
    else:
        # Paso 3: Calcular
        load_per_support = total_load / num_supports

        # Paso 4: Mostrar resultado con 2 decimales
        print(f"Load per support point: {load_per_support:.2f} N")

except (IndexError, ValueError):
    print("Error: Invalid input! Enter numeric values only.")