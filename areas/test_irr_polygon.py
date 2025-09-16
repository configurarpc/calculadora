try:
    from IrrAreas import InterfazPoligonoIrregular
except ImportError:
    print("Error: Asegúrate de que tu clase esté guardada en un archivo llamado 'IrrAreas.py'")
    exit()

def ejecutar_pruebas():
    """Función principal que ejecuta todas las pruebas."""
    print("--- Iniciando pruebas para la clase InterfazPoligonoIrregular ---")

    # --- PRUEBA 1: Cálculo de área correcto ---
    print("\n[Prueba 1: Cálculo de área de un cuadrado unitario]")
    try:
        # Vértices de un cuadrado de 1x1. El área esperada es 1.0.
        vertices_cuadrado = [(0, 0), (1, 0), (1, 1), (0, 1)]
        poligono_prueba = InterfazPoligonoIrregular(vertices_cuadrado)

        area_calculada = poligono_prueba.calcular_area()
        area_esperada = 1.0

        # Comprobar si el resultado es el correcto
        if area_calculada == area_esperada:
            print(f" ÉXITO: El área calculada ({area_calculada}) es igual a la esperada ({area_esperada}).")
        else:
            print(f" FALLO: El área calculada ({area_calculada}) NO es igual a la esperada ({area_esperada}).")

    except Exception as e:
        print(f" FALLO: La prueba generó un error inesperado: {e}")

    # --- PRUEBA 2: Error con menos de 3 vértices ---
    print("\n[Prueba 2: Creación de polígono inválido]")
    try:
        # Intentar crear un polígono con solo 2 vértices
        vertices_invalidos = [(0, 0), (1, 1)]
        _ = InterfazPoligonoIrregular(vertices_invalidos)

        # Si el código llega aquí, la prueba falló porque no se lanzó el error esperado.
        print(" FALLO: La clase NO lanzó un error al recibir menos de 3 vértices.")

    except ValueError as e:
        # Si se captura un ValueError, la prueba es exitosa.
        print(f" ÉXITO: La clase lanzó correctamente un error: '{e}'")
    except Exception as e:
        print(f" FALLO: Se lanzó un error diferente al esperado: {e}")

    print("\n--- Pruebas finalizadas ---")


# Ejecutar las pruebas al correr el script
if __name__ == "__main__":
    ejecutar_pruebas()
