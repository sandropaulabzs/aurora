from engine.terrain.generator import TerrainGenerator
from engine.terrain.world_map import WorldMap


def test_terrain_generator_creates_vertical_gradient() -> None:
    world_map = WorldMap(width=4, height=4)
    generator = TerrainGenerator()

    generator.generate(world_map)

    top_left = world_map.get_tile(0, 0)
    middle_left = world_map.get_tile(0, 2)
    bottom_left = world_map.get_tile(0, 3)

    assert top_left is not None
    assert middle_left is not None
    assert bottom_left is not None

    assert top_left.altitude == 0.0
    assert middle_left.altitude == 2 / 3
    assert bottom_left.altitude == 1.0


def test_terrain_generator_applies_same_altitude_across_each_row() -> None:
    world_map = WorldMap(width=5, height=3)
    generator = TerrainGenerator()

    generator.generate(world_map)

    row_altitudes = {
        world_map.get_tile(x, 1).altitude
        for x in range(world_map.width)
        if world_map.get_tile(x, 1) is not None
    }

    assert row_altitudes == {0.5}