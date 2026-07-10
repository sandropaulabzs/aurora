from engine.terrain.generator import TerrainGenerator
from engine.terrain.world_map import WorldMap
from engine.terrain.world_seed import WorldSeed


class World:
    """
    Representa o mundo Aurora e seus dados principais.
    """

    def __init__(
        self,
        name: str = "Aurora Zero",
        width: int = 64,
        height: int = 64,
        seed: WorldSeed | None = None,
    ) -> None:
        self.name = name
        self.seed = seed if seed is not None else WorldSeed.random()

        self.map = WorldMap(
            width=width,
            height=height,
        )

        self.terrain_generator = TerrainGenerator()

    def initialize(self) -> None:
        self.terrain_generator.generate(self.map)

        print(
            f"World '{self.name}' initialized "
            f"with map {self.map.width}x{self.map.height}."
        )

        print(f"World Seed: {self.seed.value}")