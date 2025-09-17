class Aritmetica:
    def __init__(self):
        self.ultimo_resultado = 0  # guarda el último valor calculado

    def sumar(self, a, b):
        self.ultimo_resultado = a + b
        return self.ultimo_resultado

    def restar(self, a, b):
        self.ultimo_resultado = a - b
        return self.ultimo_resultado

    def ejecutar(self):
        while True:
            print("\n--- CALCULADORA ---")
            print("1. Sumar")
            print("2. Restar")
            print("3. Mostrar último resultado")
            print("4. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "4":
                print("¡Adiós!")
                break

            elif opcion == "3":
                print(f"Último resultado: {self.ultimo_resultado}")

            elif opcion in ["1", "2"]:
                try:
                    num1 = float(input("Ingresa el primer número: "))
                    num2 = float(input("Ingresa el segundo número: "))

                    if opcion == "1":
                        print(f"Resultado: {self.sumar(num1, num2)}")
                    elif opcion == "2":
                        print(f"Resultado: {self.restar(num1, num2)}")

                except ValueError:
                    print("Error: Debes ingresar números válidos.")

            else:
                print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    arit = Aritmetica()
    arit.ejecutar()