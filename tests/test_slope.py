import pytest

from engine.terrain.slope import calculate_slope
from engine.terrain.tile import Tile


def test_positive_slope_when_target_is_lower() -> None:
    origin = Tile(x=0, y=0, altitude=0.8)
    target = Tile(x=1, y=0, altitude=0.3)

    assert calculate_slope(origin, target) == pytest.approx(0.5)


def test_negative_slope_when_target_is_higher() -> None:
    origin = Tile(x=0, y=0, altitude=0.2)
    target = Tile(x=1, y=0, altitude=0.7)

    assert calculate_slope(origin, target) == pytest.approx(-0.5)


def test_zero_slope_when_altitudes_are_equal() -> None:
    origin = Tile(x=0, y=0, altitude=0.4)
    target = Tile(x=1, y=0, altitude=0.4)

    assert calculate_slope(origin, target) == pytest.approx(0.0)