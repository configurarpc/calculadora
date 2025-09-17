# Raw_Lecture.py
"""
Utilidades de lectura/validación por consola para el proyecto de Áreas.

Características:
- Admite coma o punto como separador decimal (p. ej., "3,5" -> 3.5).
- Lectura de float/int con límites opcionales y variantes positivas.
- Lectura de opciones de menú en un rango [0..N].
- Confirmaciones sí/no.
- Lecturas compuestas (varios parámetros) manteniendo el orden.

Uso típico:
    from Raw_Lecture import RL

    r  = RL.float_pos("Ingrese el radio: ", allow_zero=False)
    op = RL.menu_option(3)  # acepta 0..3
    ok = RL.yes_no("¿Desea continuar? (s/n): ")
"""

from typing import Optional, Iterable, Dict, Tuple


class RL:
    # ====================== Normalización ======================
    @staticmethod
    def _normalize_decimal(texto: str) -> str:
        """Reemplaza coma por punto y recorta espacios."""
        return texto.strip().replace(",", ".")

    # ====================== Lecturas numéricas ======================
    @staticmethod
    def float_any(
        prompt: str,
        *,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None
    ) -> float:
        """
        Lee un float (admite coma/punto). Aplica límites si se especifican.
        Reintenta hasta que la entrada sea válida.
        """
        while True:
            raw = input(prompt)
            try:
                val = float(RL._normalize_decimal(raw))
            except ValueError:
                print("Error: Debe ingresar un valor numérico válido.")
                continue

            if min_value is not None and val < min_value:
                print(f"Error: El valor debe ser ≥ {min_value}.")
                continue
            if max_value is not None and val > max_value:
                print(f"Error: El valor debe ser ≤ {max_value}.")
                continue
            return val

    @staticmethod
    def float_pos(prompt: str, *, allow_zero: bool = True) -> float:
        """
        Lee un float no negativo si allow_zero=True, o estrictamente positivo si False.
        """
        min_v = 0.0 if allow_zero else 1e-15
        return RL.float_any(prompt, min_value=min_v)

    @staticmethod
    def int_any(
        prompt: str,
        *,
        min_value: Optional[int] = None,
        max_value: Optional[int] = None
    ) -> int:
        """
        Lee un entero con límites opcionales. Reintenta hasta que sea válido.
        """
        while True:
            raw = input(prompt).strip()

            # Permite signo positivo explícito
            if raw.startswith("+"):
                raw = raw[1:]

            # Validación general de entero (permite negativo si no se dan límites positivos)
            if not (raw.lstrip("-").isdigit()):
                print("Error: Debe ingresar un número entero válido.")
                continue

            val = int(raw)

            if min_value is not None and val < min_value:
                print(f"Error: El valor debe ser ≥ {min_value}.")
                continue
            if max_value is not None and val > max_value:
                print(f"Error: El valor debe ser ≤ {max_value}.")
                continue
            return val

    @staticmethod
    def int_pos(prompt: str, *, allow_zero: bool = True) -> int:
        """
        Lee un entero no negativo si allow_zero=True, o estrictamente positivo si False.
        """
        min_v = 0 if allow_zero else 1
        return RL.int_any(prompt, min_value=min_v)

    # ====================== Menús y confirmaciones ======================
    @staticmethod
    def menu_option(max_opt: int, prompt: str = "Seleccione una opción: ") -> int:
        """
        Lee una opción de menú en el rango [0, max_opt].
        Ej.: si max_opt=3, acepta 0,1,2,3.
        """
        while True:
            raw = input(prompt).strip()
            if not raw.isdigit():
                print("Error: Debe ingresar un número.")
                continue
            val = int(raw)
            if 0 <= val <= max_opt:
                return val
            print(f"Opción no válida. Ingrese un número entre 0 y {max_opt}.")

    @staticmethod
    def yes_no(prompt: str = "¿Confirmar? (s/n): ") -> bool:
        """
        Devuelve True si la respuesta es afirmativa (s/si/sí/y/yes).
        """
        while True:
            ans = input(prompt).strip().lower()
            if ans in {"s", "si", "sí", "y", "yes"}:
                return True
            if ans in {"n", "no"}:
                return False
            print("Responda con 's' o 'n'.")

    # ====================== Lecturas compuestas ======================
    @staticmethod
    def read_many_pos(nombres: Iterable[str], *, allow_zero: bool = True) -> Dict[str, float]:
        """
        Pide varios parámetros positivos (por nombre) y devuelve un dict {nombre: valor}.
        Ej.: RL.read_many_pos(["el radio", "la altura"], allow_zero=False)
        """
        out: Dict[str, float] = {}
        for nombre in nombres:
            out[nombre] = RL.float_pos(f"Ingrese {nombre}: ", allow_zero=allow_zero)
        return out

    @staticmethod
    def read_tuple_pos(nombres: Iterable[str], *, allow_zero: bool = True) -> Tuple[float, ...]:
        """
        Igual que read_many_pos pero devuelve tupla manteniendo el orden.
        Ej.: r, h = RL.read_tuple_pos(["el radio de la base", "la altura"], allow_zero=False)
        """
        vals = []
        for nombre in nombres:
            vals.append(RL.float_pos(f"Ingrese {nombre}: ", allow_zero=allow_zero))
        return tuple(vals)

    # ====================== Utilidad ======================
    @staticmethod
    def pause(msg: str = "Presione Enter para continuar...") -> None:
        input(msg)
