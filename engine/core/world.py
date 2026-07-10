from engine.terrain.generator import TerrainGenerator
from engine.terrain.world_map import WorldMap


class World:
    """
    Representa o mundo Aurora e seus dados principais.
    """

    def __init__(
        self,
        name: str = "Aurora Zero",
        width: int = 64,
        height: int = 64,
    ) -> None:
        self.name = name
        self.map = WorldMap(width=width, height=height)
        self.terrain_generator = TerrainGenerator()

    def initialize(self) -> None:
        self.terrain_generator.generate(self.map)

        print(
            f"World '{self.name}' initialized "
            f"with map {self.map.width}x{self.map.height}."
        )