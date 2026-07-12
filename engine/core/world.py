from engine.atmosphere.solar_radiation import SolarRadiation
from engine.terrain.generator import TerrainGenerator
from engine.terrain.planet_dna_factory import PlanetDNAFactory
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

        self.dna = PlanetDNAFactory().create(self.seed)

        self.map = WorldMap(
            width=width,
            height=height,
        )

        self.terrain_generator = TerrainGenerator()
        self.solar_radiation = SolarRadiation()

    def initialize(self) -> None:
        self.terrain_generator.generate(
            world_map=self.map,
            seed=self.seed,
            dna=self.dna,
        )

        self.solar_radiation.apply(self.map)

        print(
            f"World '{self.name}' initialized "
            f"with map {self.map.width}x{self.map.height}."
        )

        print(f"World Seed: {self.seed.value}")