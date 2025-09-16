import math
"""Importa la librería math para usar PI en los cálculos 3D."""

class Areas3D:
    """Esta clase maneja el menú y los cálculos de áreas 3D."""

    def menu(self):
        """Muestra un menú generado dinámicamente y maneja la selección."""

        while True:
            print("\n--- Menú Áreas 3D ---")

            # 1. Obtenemos los nombres de los métodos (excluyendo a menu).
            metodos_figuras = [
                metodo for metodo in dir(self) 
                if not metodo.startswith('__') and metodo != 'menu'
            ]

            # 2. Mostramos los métodos como opciones.
            for i, nombre_figura in enumerate(metodos_figuras, 1):
                print(f"{i}. {nombre_figura.replace('_', ' ').capitalize()}")

            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            try:
                opcion_num = int(opcion)

                if opcion_num == 0:
                    print("Volviendo al menú principal...")
                    break

                # 3. Verificamos que la opción esté en el rango de figuras disponibles.
                if 0 < opcion_num <= len(metodos_figuras):
                    # 4. Llamamos dinámicamente al método con getattr().
                    nombre_metodo = metodos_figuras[opcion_num - 1]
                    metodo_a_llamar = getattr(self, nombre_metodo)
                    resultado = metodo_a_llamar()

                    if resultado is not None:
                        print(f"Resultado: El área superficial del {nombre_metodo.replace('_', ' ')} es {resultado:.2f}")
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

            except ValueError:
                print("Error: Debe ingresar un número.")

    def area_cubo(self):
        """Pide datos y calcula el área superficial de un cubo."""
        try:
            lado = float(input("Ingrese el lado del cubo: "))
            if lado < 0:
                print("Error: El lado no puede ser negativo.")
                return None
            return 6 * (lado ** 2)
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un valor numérico.")
            return None

    def area_esfera(self):
        """Pide datos y calcula el área superficial de una esfera."""
        try:
            radio = float(input("Ingrese el radio de la esfera: "))
            if radio < 0:
                print("Error: El radio no puede ser negativo.")
                return None
            return 4 * math.pi * (radio ** 2)
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un valor numérico.")
            return None

    def area_cilindro(self):
        """Pide datos y calcula el área superficial de un cilindro."""
        try:
            radio = float(input("Ingrese el radio de la base del cilindro: "))
            altura = float(input("Ingrese la altura del cilindro: "))
            if radio < 0 or altura < 0:
                print("Error: Las dimensiones no pueden ser negativas.")
                return None
            return 2 * math.pi * radio * (radio + altura)
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar valores numéricos.")
            return None


if __name__ == "__main__":
    """Bloque para test: solo se ejecuta si corres el archivo directamente."""
    calculador_areas3D = Areas3D()
    calculador_areas3D.menu()
