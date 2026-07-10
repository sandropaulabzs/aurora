from engine.terrain.noise import NoiseGenerator
from engine.terrain.planet_dna import PlanetDNA
from engine.terrain.world_seed import WorldSeed


class PlanetDNAFactory:
    """
    Cria um PlanetDNA determinístico a partir de uma WorldSeed.
    """

    def create(self, seed: WorldSeed) -> PlanetDNA:
        noise = NoiseGenerator(seed)

        return PlanetDNA(
            continentality=noise.value(0, 0),
            relief=noise.value(1, 0),
            volcanism=noise.value(2, 0),
            humidity=noise.value(3, 0),
            temperature=noise.value(4, 0),
            erosion=noise.value(5, 0),
            water_level=noise.value(6, 0),
            stability=noise.value(7, 0),
        )