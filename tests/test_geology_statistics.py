import pytest

from engine.terrain.geology_statistics import GeologyStatistics
from engine.terrain.world_map import WorldMap


def test_average_altitude() -> None:
    world_map = WorldMap(width=2, height=2)

    values = [
        0.2, 0.4,
        0.6, 0.8,
    ]

    index = 0

    for row in world_map.tiles:
        for tile in row:
            tile.altitude = values[index]
            index += 1

    statistics = GeologyStatistics(world_map)

    assert statistics.average_altitude() == pytest.approx(0.5)


def test_highest_altitude() -> None:
    world_map = WorldMap(width=2, height=2)

    values = [
        0.3, 0.9,
        0.2, 0.7,
    ]

    index = 0

    for row in world_map.tiles:
        for tile in row:
            tile.altitude = values[index]
            index += 1

    statistics = GeologyStatistics(world_map)

    assert statistics.highest_altitude() == pytest.approx(0.9)


def test_lowest_altitude() -> None:
    world_map = WorldMap(width=2, height=2)

    values = [
        0.3, 0.9,
        0.2, 0.7,
    ]

    index = 0

    for row in world_map.tiles:
        for tile in row:
            tile.altitude = values[index]
            index += 1

    statistics = GeologyStatistics(world_map)

    assert statistics.lowest_altitude() == pytest.approx(0.2)