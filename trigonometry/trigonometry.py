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
        """Convierte grados a radianes"""
        return math.radians(grados)

    def _radianes_a_grados(self, radianes):
        """Convierte radianes a grados"""
        return math.degrees(radianes)

    # --- Funciones Trigonométricas Principales ---
    def seno(self, angulo):
        """Calcula el seno de un angulo o un radian"""
        angulo_en_radianes = angulo if self.mode == 'radianes' else self._grados_a_radianes(angulo)
        return math.sin(angulo_en_radianes)

   
   
    # --- (NUEVO) Funciones Trigonométricas Recíprocas ---
    def cosecante(self, angulo):
        """Calcula la cosecante (1 / seno)."""
        seno_val = self.seno(angulo)
        if seno_val == 0:
            return float('inf') # Indeterminado (división por cero)
        return 1 / seno_val

    

    # --- Funciones Trigonométricas Inversas Principales ---
    def arcoseno(self, valor):
        if not -1 <= valor <= 1:
            raise ValueError("El valor para arcoseno debe estar entre -1 y 1.")
        resultado_rad = math.asin(valor)
        return self._radianes_a_grados(resultado_rad) if self.mode == 'grados' else resultado_rad

    

    # --- (NUEVO) Funciones Trigonométricas Inversas Recíprocas ---
    def arcocosecante(self, valor):
        """Calcula la arcocosecante (arcoseno de 1/valor)."""
        if -1 < valor < 1:
            raise ValueError("El valor para arcocosecante debe ser >= 1 o <= -1.")
        return self.arcoseno(1 / valor)

    
    