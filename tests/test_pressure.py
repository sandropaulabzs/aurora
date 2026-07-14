from engine.atmosphere.atmosphere import Atmosphere
from engine.atmosphere.pressure import PressureModel
from engine.terrain.world_map import WorldMap


def test_pressure_stays_between_zero_and_one() -> None:
    world_map = WorldMap(width=4, height=4)

    atmosphere = Atmosphere(
        density=0.8,
        heat_capacity=0.6,
        pressure=0.7,
        moisture_capacity=0.5,
    )

    PressureModel().apply(
        world_map=world_map,
        atmosphere=atmosphere,
    )

    for row in world_map.tiles:
        for tile in row:
            assert 0.0 <= tile.pressure <= 1.0


def test_higher_altitude_has_lower_pressure() -> None:
    world_map = WorldMap(width=2, height=1)

    low_tile = world_map.get_tile(0, 0)
    high_tile = world_map.get_tile(1, 0)

    assert low_tile is not None
    assert high_tile is not None

    low_tile.altitude = 0.1
    high_tile.altitude = 0.9

    low_tile.temperature = 20.0
    high_tile.temperature = 20.0

    atmosphere = Atmosphere(
        density=0.8,
        heat_capacity=0.6,
        pressure=0.7,
        moisture_capacity=0.5,
    )

    PressureModel().apply(world_map, atmosphere)

    assert low_tile.pressure > high_tile.pressure


def test_colder_tile_has_higher_pressure() -> None:
    world_map = WorldMap(width=2, height=1)

    cold_tile = world_map.get_tile(0, 0)
    warm_tile = world_map.get_tile(1, 0)

    assert cold_tile is not None
    assert warm_tile is not None

    cold_tile.altitude = 0.2
    warm_tile.altitude = 0.2

    cold_tile.temperature = -10.0
    warm_tile.temperature = 40.0

    atmosphere = Atmosphere(
        density=0.8,
        heat_capacity=0.6,
        pressure=0.7,
        moisture_capacity=0.5,
    )

    PressureModel().apply(world_map, atmosphere)

    assert cold_tile.pressure > warm_tile.pressure