from engine.atmosphere.atmosphere import Atmosphere
from engine.terrain.generator import TerrainGenerator
from engine.terrain.ocean_initializer import OceanInitializer
from engine.terrain.planet_dna_factory import PlanetDNAFactory
from engine.terrain.sea_level import SeaLevel
from engine.terrain.world_map import WorldMap
from engine.terrain.world_seed import WorldSeed


class World:
    """
    Represents the Aurora world and its primary state.
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

        self.sea_level = SeaLevel(
            self.dna.water_level
        )

        self.atmosphere = Atmosphere(
            density=0.75,
            heat_capacity=0.60,
            pressure=0.70,
            moisture_capacity=0.50,
        )

        self.map = WorldMap(
            width=width,
            height=height,
        )

        # Genesis systems
        self.terrain_generator = TerrainGenerator()
        self.ocean_initializer = OceanInitializer()

    def initialize(self) -> None:
        """
        Executes only the processes that define
        the initial formation of the world.
        """

        self.terrain_generator.generate(
            world_map=self.map,
            seed=self.seed,
            dna=self.dna,
        )

        self.ocean_initializer.apply(
            world_map=self.map,
            sea_level=self.sea_level,
        )

        print(
            f"World '{self.name}' initialized "
            f"with map {self.map.width}x{self.map.height}."
        )

        print(f"World Seed: {self.seed.value}")
        print(f"Sea Level: {self.sea_level.value:.3f}")