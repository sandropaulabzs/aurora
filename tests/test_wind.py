import pytest

from engine.atmosphere.wind import WindVector


def test_wind_vector_stores_direction_and_speed() -> None:
    wind = WindVector(
        dx=1,
        dy=-1,
        speed=0.75,
    )

    assert wind.dx == 1
    assert wind.dy == -1
    assert wind.speed == pytest.approx(0.75)


def test_wind_vector_is_immutable() -> None:
    wind = WindVector(
        dx=1,
        dy=0,
        speed=0.50,
    )

    with pytest.raises(AttributeError):
        wind.speed = 0.90