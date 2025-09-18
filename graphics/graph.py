from .Function_plotting import FunctionPlotter
from .Raw_Lecture import DataPlotter


class Graph:
    def mostrar_menu(self):
        while True:
            print("\n--- Menú del gráficador ---")
            print("1. Graficar funciones predeterminadas")
            print("2. Cargar archivo .dat")
            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                FunctionPlotter().menu()
            elif opcion == "2":
                DataPlotter().menu()
            elif opcion == "0":
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    Graph  = Graph()
    Graph.mostrar_menu()
