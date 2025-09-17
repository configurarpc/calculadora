import pandas as pd
import matplotlib.pyplot as plt
import os

class DataPlotter:
    def __init__(self):
        self.filename = 'temp_data_plotter.py'
        
    def menu(self):
        """Menú para la funcionalidad de graficar datos desde un archivo."""
        while True:
            print("\n--- Menú de Gráficos desde Archivo ---")
            print("1. Graficar datos desde un archivo .dat")
            print("0. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                ruta_archivo = input("Ingrese la ruta del archivo .dat: ")
                self.create_plot_script(ruta_archivo)
            elif opcion == '0':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")

    def create_plot_script(self, ruta_archivo):
        """Genera el script para leer y graficar los datos del archivo."""
        # Sanitizar la ruta del archivo para que funcione en el script generado
        safe_ruta_archivo = ruta_archivo.replace('\\', '/')
        
        script_content = f"""
import pandas as pd
import matplotlib.pyplot as plt
import os

def leer_datos_y_graficar(ruta_archivo):
    \"\"\"
    Lee un archivo .dat con dos columnas (x y f(x)) y genera la gráfica.
    \"\"\"
    try:
        if not os.path.exists(ruta_archivo):
            print(f"Error: El archivo '{{ruta_archivo}}' no existe.")
            return

        data = pd.read_csv(ruta_archivo, delim_whitespace=True, header=None, names=['x', 'f(x)'])

        if data.empty:
            print("El archivo está vacío o no tiene datos válidos.")
            return

        print("\\nDatos cargados (primeras filas):")
        print(data.head())

        plt.figure(figsize=(8, 6))
        plt.plot(data['x'], data['f(x)'], marker='o', linestyle='-', color='b', label='f(x)')
        plt.title('Gráfico de x vs f(x) desde {os.path.basename(ruta_archivo)}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error al procesar el archivo: {{e}}")

# La ruta del archivo se pasa al generar el script
leer_datos_y_graficar('{safe_ruta_archivo}')
"""
        with open(self.filename, 'w') as file:
            file.write(script_content)
        print(f"Script de graficación generado en '{self.filename}'.")

    def execute_plotter(self):
        """Ejecuta el script de graficación temporal."""
        try:
            # Importar subprocess aquí para evitar problemas de dependencia circular
            import subprocess
            subprocess.run(["python", self.filename], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script: {e}")
        except FileNotFoundError:
            print("El comando 'python' no se encontró. Asegúrese de que Python esté en su PATH.")

    def clean_up(self):
        """Elimina el archivo temporal si existe."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"Archivo '{self.filename}' eliminado.")

# Uso del script
if __name__ == "__main__":
    plotter = DataPlotter()
    
    # Este bloque maneja la lógica de ejecución del menú principal
    try:
        plotter.menu()
    finally:
        plotter.clean_up()

