import pytest

from engine.hydrology.infiltration import InfiltrationModel
from engine.terrain.world_map import WorldMap


def test_infiltration_moves_surface_water_into_soil() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.surface_water = 1.0
    tile.ground_moisture = 0.20
    tile.soil_capacity = 1.0

    InfiltrationModel().apply(
        world_map,
        infiltration_rate=0.25,
    )

    assert tile.surface_water == pytest.approx(0.75)
    assert tile.ground_moisture == pytest.approx(0.45)


def test_infiltration_is_limited_by_available_soil_capacity() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.surface_water = 0.50
    tile.ground_moisture = 0.90
    tile.soil_capacity = 1.0

    InfiltrationModel().apply(
        world_map,
        infiltration_rate=0.50,
    )

    assert tile.infiltration == pytest.approx(0.10)
    assert tile.ground_moisture == pytest.approx(1.0)
    assert tile.surface_water == pytest.approx(0.40)


def test_saturated_soil_does_not_infiltrate() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.surface_water = 0.60
    tile.ground_moisture = 1.0
    tile.soil_capacity = 1.0
    tile.infiltration = 0.25

    InfiltrationModel().apply(world_map)

    assert tile.infiltration == pytest.approx(0.0)
    assert tile.ground_moisture == pytest.approx(1.0)
    assert tile.surface_water == pytest.approx(0.60)


def test_infiltration_conserves_total_water() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.surface_water = 0.80
    tile.ground_moisture = 0.30
    tile.soil_capacity = 1.0

    total_before = (
        tile.surface_water
        + tile.ground_moisture
    )

    InfiltrationModel().apply(
        world_map,
        infiltration_rate=0.10,
    )

    total_after = (
        tile.surface_water
        + tile.ground_moisture
    )

    assert total_after == pytest.approx(total_before)


def test_infiltration_records_current_tick_amount() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.surface_water = 0.80
    tile.soil_capacity = 1.0

    InfiltrationModel().apply(
        world_map,
        infiltration_rate=0.25,
    )

    assert tile.infiltration == pytest.approx(0.20)


def test_no_surface_water_resets_infiltration_to_zero() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.surface_water = 0.0
    tile.ground_moisture = 0.40
    tile.soil_capacity = 1.0
    tile.infiltration = 0.30

    InfiltrationModel().apply(world_map)

    assert tile.surface_water == pytest.approx(0.0)
    assert tile.ground_moisture == pytest.approx(0.40)
    assert tile.infiltration == pytest.approx(0.0)


@pytest.mark.parametrize(
    "invalid_rate",
    [-0.01, 1.01],
)
def test_invalid_infiltration_rate_raises_error(
    invalid_rate: float,
) -> None:
    world_map = WorldMap(width=1, height=1)

    with pytest.raises(ValueError):
        InfiltrationModel().apply(
            world_map,
            infiltration_rate=invalid_rate,
        )