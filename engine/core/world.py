from engine.atmosphere.atmosphere import Atmosphere
from engine.atmosphere.solar_radiation import SolarRadiation
from engine.atmosphere.temperature import TemperatureModel
from engine.terrain.generator import TerrainGenerator
from engine.terrain.planet_dna_factory import PlanetDNAFactory
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

        self.terrain_generator = TerrainGenerator()
        self.solar_radiation = SolarRadiation()
        self.temperature_model = TemperatureModel()

    def initialize(self) -> None:
        self.terrain_generator.generate(
            world_map=self.map,
            seed=self.seed,
            dna=self.dna,
        )

        self.solar_radiation.apply(self.map)

        self.temperature_model.apply(
            world_map=self.map,
            atmosphere=self.atmosphere,
        )

        print(
            f"World '{self.name}' initialized "
            f"with map {self.map.width}x{self.map.height}."
        )

        print(f"World Seed: {self.seed.value}")