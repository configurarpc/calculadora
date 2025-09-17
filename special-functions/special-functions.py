"""
Módulo: special_functions
Contiene funciones especiales para cálculos logarítmicos,
exponenciales y de potencias.
"""

import math

# ========================
# Funciones Logarítmicas
# ========================

def log_base_e(x: float) -> float:
    """
    Calcula el logaritmo natural (base e).
    """
    if x <= 0:
        raise ValueError("El logaritmo natural no está definido para valores <= 0.")
    return math.log(x)


def log_base_10(x: float) -> float:
    """
    Calcula el logaritmo en base 10.
    """
    if x <= 0:
        raise ValueError("El logaritmo base 10 no está definido para valores <= 0.")
    return math.log10(x)


def log_base(x: float, base: float) -> float:
    """
    Calcula el logaritmo en una base arbitraria.
    """
    if x <= 0:
        raise ValueError("El logaritmo no está definido para valores <= 0.")
    if base <= 0 or base == 1:
        raise ValueError("La base del logaritmo debe ser positiva y distinta de 1.")
    return math.log(x, base)

# ========================
# Funciones Exponenciales
# ========================

def exp_e(x: float) -> float:
    """
    Calcula e^x.
    """
    return math.exp(x)


def exp_base(base: float, x: float) -> float:
    """
    Calcula base^x.
    """
    return math.pow(base, x)


# ========================
# Funciones Potenciales
# ========================

def power(base: float, exponent: float) -> float:
    """
    Calcula base elevado a la potencia exponent.
    """
    return math.pow(base, exponent)


def sqrt(x: float) -> float:
    """
    Calcula la raíz cuadrada.
    """
    if x < 0:
        raise ValueError("La raíz cuadrada no está definida para números negativos en R.")
    return math.sqrt(x)