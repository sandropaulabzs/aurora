from engine.terrain.direction import Direction
from engine.terrain.tile import Tile


class WorldMap:
    """
    Representa o mapa do mundo.
    """

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.tiles = [
            [
                Tile(x=x, y=y)
                for x in range(width)
            ]
            for y in range(height)
        ]

    def get_tile(self, x: int, y: int) -> Tile | None:
        """
        Retorna uma Tile ou None caso esteja fora dos limites.
        """

        if not self.in_bounds(x, y):
            return None

        return self.tiles[y][x]

    def in_bounds(self, x: int, y: int) -> bool:
        """
        Verifica se uma posição pertence ao mapa.
        """

        return (
            0 <= x < self.width
            and 0 <= y < self.height
        )

    def get_neighbors(self, x: int, y: int) -> list[Tile]:
        """
        Retorna todas as Tiles vizinhas válidas da posição informada.
        """

        neighbors: list[Tile] = []

        for direction in Direction:
            offset_x, offset_y = direction.offset

            neighbor = self.get_tile(
                x + offset_x,
                y + offset_y,
            )

            if neighbor is not None:
                neighbors.append(neighbor)

        return neighbors