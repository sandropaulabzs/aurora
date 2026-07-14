import pytest

from engine.hydrology.evaporation_transfer import EvaporationTransfer
from engine.terrain.world_map import WorldMap


def test_evaporation_transfer_moves_water_to_atmosphere() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.ground_moisture = 1.0
    tile.evaporation = 0.8
    tile.atmospheric_moisture = 0.0

    EvaporationTransfer().apply(
        world_map,
        transfer_rate=0.5,
    )

    assert tile.ground_moisture == pytest.approx(0.6)
    assert tile.atmospheric_moisture == pytest.approx(0.4)


def test_evaporation_transfer_conserves_water() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.ground_moisture = 0.75
    tile.evaporation = 0.4
    tile.atmospheric_moisture = 0.20

    total_before = (
        tile.ground_moisture
        + tile.atmospheric_moisture
    )

    EvaporationTransfer().apply(
        world_map,
        transfer_rate=0.25,
    )

    total_after = (
        tile.ground_moisture
        + tile.atmospheric_moisture
    )

    assert total_after == pytest.approx(total_before)


def test_transfer_never_exceeds_available_ground_water() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.ground_moisture = 0.1
    tile.evaporation = 1.0

    EvaporationTransfer().apply(
        world_map,
        transfer_rate=1.0,
    )

    assert tile.ground_moisture >= 0.0
    assert tile.atmospheric_moisture <= 0.1


def test_invalid_transfer_rate_raises_error() -> None:
    world_map = WorldMap(width=1, height=1)

    with pytest.raises(ValueError):
        EvaporationTransfer().apply(
            world_map,
            transfer_rate=1.5,
        )