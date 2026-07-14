import pytest

from engine.atmosphere.precipitation_threshold import (
    PrecipitationThresholdModel,
)
from engine.terrain.world_map import WorldMap


def test_warm_air_requires_more_cloud_water() -> None:
    world_map = WorldMap(width=2, height=1)

    cold = world_map.get_tile(0, 0)
    hot = world_map.get_tile(1, 0)

    assert cold is not None
    assert hot is not None

    cold.temperature = 0.0
    hot.temperature = 40.0

    PrecipitationThresholdModel().apply(world_map)

    assert (
        hot.precipitation_threshold
        >
        cold.precipitation_threshold
    )


def test_threshold_is_normalized() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.temperature = 150.0

    PrecipitationThresholdModel().apply(world_map)

    assert (
        0.20
        <= tile.precipitation_threshold
        <= 0.70
    )


def test_cold_air_has_minimum_threshold() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.temperature = -100.0

    PrecipitationThresholdModel().apply(world_map)

    assert tile.precipitation_threshold == pytest.approx(0.20)