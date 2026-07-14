import pytest

from engine.atmosphere.pressure_gradient import (
    calculate_pressure_gradient,
)
from engine.terrain.tile import Tile


def test_positive_gradient_when_target_has_lower_pressure() -> None:
    origin = Tile(
        x=0,
        y=0,
        pressure=0.8,
    )

    target = Tile(
        x=1,
        y=0,
        pressure=0.3,
    )

    gradient = calculate_pressure_gradient(
        origin,
        target,
    )

    assert gradient == pytest.approx(0.5)


def test_negative_gradient_when_target_has_higher_pressure() -> None:
    origin = Tile(
        x=0,
        y=0,
        pressure=0.2,
    )

    target = Tile(
        x=1,
        y=0,
        pressure=0.7,
    )

    gradient = calculate_pressure_gradient(
        origin,
        target,
    )

    assert gradient == pytest.approx(-0.5)


def test_zero_gradient_when_pressures_are_equal() -> None:
    origin = Tile(
        x=0,
        y=0,
        pressure=0.4,
    )

    target = Tile(
        x=1,
        y=0,
        pressure=0.4,
    )

    gradient = calculate_pressure_gradient(
        origin,
        target,
    )

    assert gradient == pytest.approx(0.0)