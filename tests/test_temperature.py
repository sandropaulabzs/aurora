import pytest

from engine.atmosphere.atmosphere import Atmosphere
from engine.atmosphere.temperature import TemperatureModel
from engine.terrain.world_map import WorldMap


def test_temperature_stays_within_expected_range() -> None:
    world_map = WorldMap(width=4, height=4)

    atmosphere = Atmosphere(
        density=0.8,
        heat_capacity=0.6,
        pressure=0.7,
        moisture_capacity=0.5,
    )

    TemperatureModel().apply(
        world_map=world_map,
        atmosphere=atmosphere,
    )

    for row in world_map.tiles:
        for tile in row:
            assert -30.0 <= tile.temperature <= 50.0


def test_high_light_tile_is_warmer_than_low_light_tile() -> None:
    world_map = WorldMap(width=2, height=1)

    cold_tile = world_map.get_tile(0, 0)
    warm_tile = world_map.get_tile(1, 0)

    assert cold_tile is not None
    assert warm_tile is not None

    cold_tile.light = 0.1
    warm_tile.light = 0.9

    cold_tile.altitude = 0.2
    warm_tile.altitude = 0.2

    atmosphere = Atmosphere(
        density=0.8,
        heat_capacity=0.5,
        pressure=0.7,
        moisture_capacity=0.5,
    )

    TemperatureModel().apply(world_map, atmosphere)

    assert warm_tile.temperature > cold_tile.temperature


def test_higher_altitude_tile_is_colder() -> None:
    world_map = WorldMap(width=2, height=1)

    low_tile = world_map.get_tile(0, 0)
    high_tile = world_map.get_tile(1, 0)

    assert low_tile is not None
    assert high_tile is not None

    low_tile.light = 0.8
    high_tile.light = 0.8

    low_tile.altitude = 0.1
    high_tile.altitude = 0.9

    atmosphere = Atmosphere(
        density=0.8,
        heat_capacity=0.5,
        pressure=0.7,
        moisture_capacity=0.5,
    )

    TemperatureModel().apply(world_map, atmosphere)

    assert low_tile.temperature > high_tile.temperature


def test_greater_heat_capacity_retains_more_temperature() -> None:
    world_map_a = WorldMap(width=1, height=1)
    world_map_b = WorldMap(width=1, height=1)

    tile_a = world_map_a.get_tile(0, 0)
    tile_b = world_map_b.get_tile(0, 0)

    assert tile_a is not None
    assert tile_b is not None

    tile_a.light = 0.5
    tile_b.light = 0.5

    tile_a.altitude = 0.3
    tile_b.altitude = 0.3

    low_capacity = Atmosphere(
        density=0.8,
        heat_capacity=0.1,
        pressure=0.7,
        moisture_capacity=0.5,
    )

    high_capacity = Atmosphere(
        density=0.8,
        heat_capacity=0.9,
        pressure=0.7,
        moisture_capacity=0.5,
    )

    model = TemperatureModel()

    model.apply(world_map_a, low_capacity)
    model.apply(world_map_b, high_capacity)

    assert tile_b.temperature > tile_a.temperature