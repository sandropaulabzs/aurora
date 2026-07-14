import pytest

from engine.terrain.sea_level import SeaLevel


def test_valid_sea_level_is_created() -> None:
    sea_level = SeaLevel(0.35)

    assert sea_level.value == pytest.approx(0.35)


def test_zero_is_valid() -> None:
    sea_level = SeaLevel(0.0)

    assert sea_level.value == pytest.approx(0.0)


def test_one_is_valid() -> None:
    sea_level = SeaLevel(1.0)

    assert sea_level.value == pytest.approx(1.0)


def test_negative_sea_level_is_invalid() -> None:
    with pytest.raises(ValueError):
        SeaLevel(-0.01)


def test_sea_level_above_one_is_invalid() -> None:
    with pytest.raises(ValueError):
        SeaLevel(1.01)