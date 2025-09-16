import math

class CalculadoraTrigonometrica:
    """
    Una clase para una calculadora científica que puede operar en modo de
    grados ('grados') o radianes ('radianes'), incluyendo funciones recíprocas.
    """

    def __init__(self, mode='grados'):
        """
        Inicializa la calculadora.

        Args:
            mode (str): El modo de operación. Puede ser 'grados' o 'radianes'.
                        Por defecto, es 'grados'.
        """
        if mode not in ['grados', 'radianes']:
            raise ValueError("El modo debe ser 'grados' o 'radianes'")
        self.mode = mode
        print(f"Calculadora iniciada en modo: {self.mode}")

    # --- Métodos de Conversión Internos ---
    def _grados_a_radianes(self, grados):
        return math.radians(grados)

    def _radianes_a_grados(self, radianes):
        return math.degrees(radianes)

    # --- Funciones Trigonométricas Principales ---
    def seno(self, angulo):
        angulo_en_radianes = angulo if self.mode == 'radianes' else self._grados_a_radianes(angulo)
        return math.sin(angulo_en_radianes)

    def coseno(self, angulo):
        angulo_en_radianes = angulo if self.mode == 'radianes' else self._grados_a_radianes(angulo)
        return math.cos(angulo_en_radianes)

    def tangente(self, angulo):
        if self.mode == 'grados' and angulo % 180 == 90:
            return float('inf') # Indeterminado
        angulo_en_radianes = angulo if self.mode == 'radianes' else self._grados_a_radianes(angulo)
        return math.tan(angulo_en_radianes)

    # --- (NUEVO) Funciones Trigonométricas Recíprocas ---
    def cosecante(self, angulo):
        """Calcula la cosecante (1 / seno)."""
        seno_val = self.seno(angulo)
        if seno_val == 0:
            return float('inf') # Indeterminado (división por cero)
        return 1 / seno_val

    def secante(self, angulo):
        """Calcula la secante (1 / coseno)."""
        coseno_val = self.coseno(angulo)
        if coseno_val == 0:
            return float('inf') # Indeterminado (división por cero)
        return 1 / coseno_val

    def cotangente(self, angulo):
        """Calcula la cotangente (1 / tangente)."""
        tangente_val = self.tangente(angulo)
        if tangente_val == 0:
            return float('inf') # Indeterminado
        # Para evitar problemas de precisión con tangente cerca del infinito
        coseno_val = self.coseno(angulo)
        seno_val = self.seno(angulo)
        if seno_val == 0:
           return float('inf')
        return coseno_val / seno_val


    # --- Funciones Trigonométricas Inversas Principales ---
    def arcoseno(self, valor):
        if not -1 <= valor <= 1:
            raise ValueError("El valor para arcoseno debe estar entre -1 y 1.")
        resultado_rad = math.asin(valor)
        return self._radianes_a_grados(resultado_rad) if self.mode == 'grados' else resultado_rad

    def arcocoseno(self, valor):
        if not -1 <= valor <= 1:
            raise ValueError("El valor para arcocoseno debe estar entre -1 y 1.")
        resultado_rad = math.acos(valor)
        return self._radianes_a_grados(resultado_rad) if self.mode == 'grados' else resultado_rad

    def arcotangente(self, valor):
        resultado_rad = math.atan(valor)
        return self._radianes_a_grados(resultado_rad) if self.mode == 'grados' else resultado_rad

    # --- (NUEVO) Funciones Trigonométricas Inversas Recíprocas ---
    def arcocosecante(self, valor):
        """Calcula la arcocosecante (arcoseno de 1/valor)."""
        if -1 < valor < 1:
            raise ValueError("El valor para arcocosecante debe ser >= 1 o <= -1.")
        return self.arcoseno(1 / valor)

    def arcosecante(self, valor):
        """Calcula la arcosecante (arcocoseno de 1/valor)."""
        if -1 < valor < 1:
            raise ValueError("El valor para arcosecante debe ser >= 1 o <= -1.")
        return self.arcocoseno(1 / valor)

    def arcocotangente(self, valor):
        """Calcula la arcocotangente (arcotangente de 1/valor)."""
        if valor == 0:
            # El arcotangente de infinito es 90 grados o PI/2 radianes
            return 90.0 if self.mode == 'grados' else math.pi / 2
        return self.arcotangente(1 / valor)