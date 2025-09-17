# raw_lecture.py
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

def leer_datos_y_graficar(ruta_archivo):
    """
    Lee un archivo .dat con dos columnas (x y f(x)) y genera la gráfica.
    """
    try:
        # Validar que el archivo existe
        if not os.path.exists(ruta_archivo):
            print(f"Error: El archivo '{ruta_archivo}' no existe.")
            return

        # Leer archivo con pandas
        # Se asume que el archivo tiene dos columnas separadas por espacios o tabulaciones
        data = pd.read_csv(ruta_archivo, delim_whitespace=True, header=None, names=['x', 'f(x)'])

        # Validar que hay datos
        if data.empty:
            print("El archivo está vacío o no tiene datos válidos.")
            return

        # Mostrar los primeros datos
        print("\nDatos cargados (primeras filas):")
        print(data.head())

        # Graficar
        plt.figure(figsize=(8, 6))
        plt.plot(data['x'], data['f(x)'], marker='o', linestyle='-', color='b', label='f(x)')
        plt.title('Gráfico de x vs f(x)')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        # Mostrar la gráfica
        plt.show()

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python raw_lecture.py <archivo.dat>")
        return
    
    ruta_archivo = sys.argv[1]
    leer_datos_y_graficar(ruta_archivo)

if __name__ == "__main__":
    main()
