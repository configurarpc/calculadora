from areas.areas import Areas

def main():
    while True:
        print("\n=== Calculadora ===")
        print("1. Áreas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            Areas().mostrar_menu()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
if __name__ == "__main__":
    main()