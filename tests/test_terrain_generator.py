from engine.terrain.generator import TerrainGenerator
from engine.terrain.planet_dna_factory import PlanetDNAFactory
from engine.terrain.world_map import WorldMap
from engine.terrain.world_seed import WorldSeed


def test_terrain_generator_is_deterministic_for_same_seed() -> None:
    seed = WorldSeed(12345)
    dna = PlanetDNAFactory().create(seed)

    world_map_a = WorldMap(width=8, height=8)
    world_map_b = WorldMap(width=8, height=8)

    generator = TerrainGenerator()

    generator.generate(
        world_map=world_map_a,
        seed=seed,
        dna=dna,
    )

    generator.generate(
        world_map=world_map_b,
        seed=seed,
        dna=dna,
    )

    altitudes_a = [
        world_map_a.get_tile(x, y).altitude
        for y in range(world_map_a.height)
        for x in range(world_map_a.width)
        if world_map_a.get_tile(x, y) is not None
    ]

    altitudes_b = [
        world_map_b.get_tile(x, y).altitude
        for y in range(world_map_b.height)
        for x in range(world_map_b.width)
        if world_map_b.get_tile(x, y) is not None
    ]

    assert altitudes_a == altitudes_b


def test_terrain_generator_creates_altitude_variation() -> None:
    seed = WorldSeed(67890)
    dna = PlanetDNAFactory().create(seed)

    world_map = WorldMap(width=16, height=16)
    generator = TerrainGenerator()

    generator.generate(
        world_map=world_map,
        seed=seed,
        dna=dna,
    )

    altitudes = {
        world_map.get_tile(x, y).altitude
        for y in range(world_map.height)
        for x in range(world_map.width)
        if world_map.get_tile(x, y) is not None
    }

    assert len(altitudes) > 1
    assert all(0.0 <= altitude <= 1.0 for altitude in altitudes)