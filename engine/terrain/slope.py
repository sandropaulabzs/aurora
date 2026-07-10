from engine.terrain.tile import Tile


def calculate_slope(origin: Tile, target: Tile) -> float:
    """
    Calcula a diferença de altitude entre duas tiles.

    Valor positivo:
        o alvo está mais baixo.

    Valor negativo:
        o alvo está mais alto.

    Valor zero:
        ambas possuem a mesma altitude.
    """

    return origin.altitude - target.altitude