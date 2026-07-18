import pytest

from engine.hydrology.water_passage_decay import (
    WaterPassageDecayModel,
)
from engine.terrain.world_map import WorldMap


def test_water_passage_decays_proportionally() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.water_passage = 10.0

    WaterPassageDecayModel().apply(
        world_map,
        decay=0.90,
    )

    assert tile.water_passage == pytest.approx(9.0)


def test_zero_water_passage_remains_zero() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.water_passage = 0.0

    WaterPassageDecayModel().apply(
        world_map,
        decay=0.50,
    )

    assert tile.water_passage == pytest.approx(0.0)


def test_repeated_decay_reduces_memory_gradually() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.water_passage = 1.0

    model = WaterPassageDecayModel()

    for _ in range(3):
        model.apply(
            world_map,
            decay=0.50,
        )

    assert tile.water_passage == pytest.approx(0.125)


@pytest.mark.parametrize(
    "invalid_decay",
    [-0.01, 1.01],
)
def test_invalid_decay_raises_error(
    invalid_decay: float,
) -> None:
    world_map = WorldMap(width=1, height=1)

    with pytest.raises(ValueError):
        WaterPassageDecayModel().apply(
            world_map,
            decay=invalid_decay,
        )