import pytest

from engine.atmosphere.solar_radiation import SolarRadiation
from engine.terrain.world_map import WorldMap


def test_equator_receives_more_light_than_poles() -> None:
    world_map = WorldMap(width=3, height=5)

    SolarRadiation().apply(world_map)

    north = world_map.get_tile(1, 0)
    equator = world_map.get_tile(1, 2)
    south = world_map.get_tile(1, 4)

    assert north is not None
    assert equator is not None
    assert south is not None

    assert equator.light > north.light
    assert equator.light > south.light


def test_poles_receive_same_radiation() -> None:
    world_map = WorldMap(width=3, height=5)

    SolarRadiation().apply(world_map)

    north = world_map.get_tile(1, 0)
    south = world_map.get_tile(1, 4)

    assert north is not None
    assert south is not None

    assert north.light == pytest.approx(south.light)


def test_all_tiles_receive_light_between_zero_and_one() -> None:
    world_map = WorldMap(width=8, height=8)

    SolarRadiation().apply(world_map)

    for row in world_map.tiles:
        for tile in row:
            assert 0.0 <= tile.light <= 1.0


def test_invalid_world_height_raises_error() -> None:
    world_map = WorldMap(width=4, height=1)

    with pytest.raises(ValueError):
        SolarRadiation().apply(world_map)