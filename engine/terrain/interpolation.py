def lerp(a: float, b: float, t: float) -> float:
    """
    Interpolação linear entre dois valores.
    """

    return a + (b - a) * t


def smoothstep(t: float) -> float:
    """
    Suaviza a interpolação.

    Entrada:
        0.0 → 1.0

    Saída:
        curva suave.
    """

    return t * t * (3.0 - 2.0 * t)