from engine.terrain.drainage import find_lowest_neighbor
from engine.terrain.tile import Tile
from engine.terrain.world_map import WorldMap


class DrainageMap:
    """
    Mapeia o escoamento natural do relevo.

    Para cada Tile, guarda a Tile vizinha
    para onde a água tenderia a escorrer.
    """

    def __init__(self) -> None:
        self._flow: dict[tuple[int, int], Tile | None] = {}

    def generate(self, world_map: WorldMap) -> None:

        self._flow.clear()

        for y in range(world_map.height):
            for x in range(world_map.width):

                origin = world_map.get_tile(x, y)

                assert origin is not None

                self._flow[(x, y)] = find_lowest_neighbor(
                    world_map,
                    origin,
                )

    def destination(
        self,
        x: int,
        y: int,
    ) -> Tile | None:
        """
        Retorna o destino natural do escoamento
        para a posição informada.
        """

        return self._flow.get((x, y))