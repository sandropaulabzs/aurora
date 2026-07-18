import pytest

from engine.hydrology.runoff import RunoffModel
from engine.terrain.world_map import WorldMap


def test_water_flows_to_lower_neighbor() -> None:
    world_map = WorldMap(width=2, height=1)

    left = world_map.get_tile(0, 0)
    right = world_map.get_tile(1, 0)

    assert left is not None
    assert right is not None

    left.altitude = 10.0
    right.altitude = 5.0
    left.surface_water = 1.0

    RunoffModel().apply(
        world_map,
        runoff_rate=0.10,
    )

    assert left.surface_water == pytest.approx(0.90)
    assert right.surface_water == pytest.approx(0.10)


def test_water_does_not_flow_uphill() -> None:
    world_map = WorldMap(width=2, height=1)

    left = world_map.get_tile(0, 0)
    right = world_map.get_tile(1, 0)

    assert left is not None
    assert right is not None

    left.altitude = 5.0
    right.altitude = 10.0
    left.surface_water = 1.0

    RunoffModel().apply(world_map)

    assert left.surface_water == pytest.approx(1.0)
    assert right.surface_water == pytest.approx(0.0)


def test_runoff_records_current_tick_amount() -> None:
    world_map = WorldMap(width=2, height=1)

    left = world_map.get_tile(0, 0)
    right = world_map.get_tile(1, 0)

    assert left is not None
    assert right is not None

    left.altitude = 10.0
    right.altitude = 5.0
    left.surface_water = 0.80

    RunoffModel().apply(
        world_map,
        runoff_rate=0.25,
    )

    assert left.runoff == pytest.approx(0.20)
    assert right.runoff == pytest.approx(0.0)


def test_no_flow_resets_runoff_to_zero() -> None:
    world_map = WorldMap(width=2, height=1)

    left = world_map.get_tile(0, 0)
    right = world_map.get_tile(1, 0)

    assert left is not None
    assert right is not None

    left.altitude = 5.0
    right.altitude = 10.0
    left.surface_water = 1.0
    left.runoff = 0.40

    RunoffModel().apply(world_map)

    assert left.runoff == pytest.approx(0.0)


def test_runoff_conserves_total_water() -> None:
    world_map = WorldMap(width=2, height=1)

    left = world_map.get_tile(0, 0)
    right = world_map.get_tile(1, 0)

    assert left is not None
    assert right is not None

    left.altitude = 10.0
    right.altitude = 5.0
    left.surface_water = 0.80
    right.surface_water = 0.20

    total_before = (
        left.surface_water
        + right.surface_water
    )

    RunoffModel().apply(
        world_map,
        runoff_rate=0.25,
    )

    total_after = (
        left.surface_water
        + right.surface_water
    )

    assert total_after == pytest.approx(total_before)


def test_runoff_into_ocean_returns_to_ocean_reservoir() -> None:
    world_map = WorldMap(width=2, height=1)

    land = world_map.get_tile(0, 0)
    ocean = world_map.get_tile(1, 0)

    assert land is not None
    assert ocean is not None

    land.altitude = 1.0
    land.surface_water = 1.0

    ocean.altitude = 0.0
    ocean.is_ocean = True
    ocean.ground_moisture = 1.0

    RunoffModel().apply(
        world_map,
        runoff_rate=0.10,
    )

    assert land.surface_water == pytest.approx(0.90)
    assert ocean.surface_water == pytest.approx(0.0)
    assert ocean.ground_moisture == pytest.approx(1.10)


@pytest.mark.parametrize(
    "invalid_rate",
    [-0.01, 1.01],
)
def test_invalid_runoff_rate_raises_error(
    invalid_rate: float,
) -> None:
    world_map = WorldMap(width=1, height=1)

    with pytest.raises(ValueError):
        RunoffModel().apply(
            world_map,
            runoff_rate=invalid_rate,
        )