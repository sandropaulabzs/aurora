import pytest

from engine.atmosphere.atmosphere import Atmosphere


def test_atmosphere_stores_all_properties() -> None:
    atmosphere = Atmosphere(
        density=0.8,
        heat_capacity=0.7,
        pressure=0.9,
        moisture_capacity=0.6,
    )

    assert atmosphere.density == pytest.approx(0.8)
    assert atmosphere.heat_capacity == pytest.approx(0.7)
    assert atmosphere.pressure == pytest.approx(0.9)
    assert atmosphere.moisture_capacity == pytest.approx(0.6)


def test_atmosphere_is_immutable() -> None:
    atmosphere = Atmosphere(
        density=0.8,
        heat_capacity=0.7,
        pressure=0.9,
        moisture_capacity=0.6,
    )

    with pytest.raises(AttributeError):
        atmosphere.pressure = 0.2