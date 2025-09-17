from arithmetic.arithmetic import Aritmetica
from areas.areas import Areas

def main():
    while True:
        print("\n=== Calculadora ===")
        print("1. Aritmética")
        print("2. Áreas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Aritmetica().mostrar_menu()
        elif opcion == "2":
            Areas().mostrar_menu()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")  

if __name__ == "__main__":
    main()
