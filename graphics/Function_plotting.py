import numpy as np
import os
import subprocess

class FunctionPlotter:
    def __init__(self):
        self.functions = {
            1: ('Seno (sin(x))', 'np.sin(x)'),
            2: ('Coseno (cos(x))', 'np.cos(x)'),
            3: ('Exponencial (e^x)', 'np.exp(x)'),
            4: ('Logaritmo Natural (ln(x))', 'np.log(x)'),
            5: ('Función Cuadrática (x^2)', 'x**2')
        }
        self.temp_filename = 'temp_plotter.py'

    def menu(self):
        while True:
            print("\n--- Menú de Gráficos de Funciones ---")
            for key, value in self.functions.items():
                print(f"{key}. {value[0]}")
            print("0. Salir")

            try:
                opcion = int(input("Seleccione una función para graficar: "))
                if opcion == 0:
                    print("Saliendo del programa.")
                    self.clean_up()
                    break
                elif opcion in self.functions:
                    xmin, xmax, ymin, ymax = self.get_plot_ranges()
                    output_filename = input("Ingrese el nombre del archivo para guardar la imagen (ej. mi_grafica.png): ")
                    self.create_plot_script(opcion, xmin, xmax, ymin, ymax, output_filename)
                    self.execute_plotter()
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

    def get_plot_ranges(self):
        """Solicita al usuario los rangos para los ejes x e y."""
        while True:
            try:
                print("\n--- Definir Rangos del Gráfico ---")
                xmin = float(input("Ingrese el valor mínimo para X: "))
                xmax = float(input("Ingrese el valor máximo para X: "))
                ymin = float(input("Ingrese el valor mínimo para Y: "))
                ymax = float(input("Ingrese el valor máximo para Y: "))
                return xmin, xmax, ymin, ymax
            except ValueError:
                print("Entrada no válida. Por favor, ingrese valores numéricos.")

    def create_plot_script(self, choice, xmin, xmax, ymin, ymax, output_filename):
        """Genera el contenido del archivo temporal."""
        function_name, function_code = self.functions[choice]
        
        # Agregamos una validación simple para el nombre del archivo
        if not output_filename.endswith('.png') and not output_filename.endswith('.jpg'):
            output_filename += '.png'
            
        script_content = f"""
import numpy as np
import matplotlib.pyplot as plt

# Generar datos para la función
x = np.linspace({xmin}, {xmax}, 400)
y = {function_code}

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Trazar la función
ax.plot(x, y, label='{function_name}')

# Configurar los límites de los ejes
ax.set_xlim([{xmin}, {xmax}])
ax.set_ylim([{ymin}, {ymax}])

# Configurar el título y las etiquetas
ax.set_title('{function_name}')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')

# Agregar la cuadrícula y la leyenda
ax.grid(True)
ax.legend()

# Guardar la gráfica en un archivo
plt.savefig('{output_filename}')
plt.close(fig)
"""
        with open(self.temp_filename, 'w') as file:
            file.write(script_content)
        print(f"Código de gráfico guardado en '{self.temp_filename}'.")
        print(f"El gráfico se guardará como '{output_filename}'.")

    def execute_plotter(self):
        """Ejecuta el archivo temporal."""
        try:
            subprocess.run(["python3", self.temp_filename], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script: {e}")
        except FileNotFoundError:
            print("El comando 'python3' no se encontró. Asegúrese de que Python esté en su PATH.")
            
    def clean_up(self):
        """Elimina el archivo temporal si existe."""
        if os.path.exists(self.temp_filename):
            os.remove(self.temp_filename)
            print(f"Archivo temporal '{self.temp_filename}' eliminado.")

if __name__ == "__main__":
    plotter = FunctionPlotter()
    plotter.menu()
