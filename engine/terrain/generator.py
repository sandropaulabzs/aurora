from engine.terrain.planet_dna import PlanetDNA
from engine.terrain.relief_composer import ReliefComposer
from engine.terrain.world_map import WorldMap
from engine.terrain.world_seed import WorldSeed


class TerrainGenerator:
    """
    Responsável pela geração inicial do relevo.
    """

    def generate(
        self,
        world_map: WorldMap,
        seed: WorldSeed,
        dna: PlanetDNA,
    ) -> None:

        composer = ReliefComposer(seed, dna)

        for y in range(world_map.height):

            for x in range(world_map.width):

                tile = world_map.get_tile(x, y)

                assert tile is not None

                tile.altitude = composer.altitude_at(x, y)