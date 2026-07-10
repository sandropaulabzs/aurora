import pytest

from engine.terrain.planet_dna import PlanetDNA


def test_planet_dna_stores_all_genes() -> None:
    dna = PlanetDNA(
        continentality=0.8,
        relief=0.7,
        volcanism=0.6,
        humidity=0.5,
        temperature=0.4,
        erosion=0.3,
        water_level=0.2,
        stability=0.9,
    )

    assert dna.continentality == 0.8
    assert dna.relief == 0.7
    assert dna.volcanism == 0.6
    assert dna.humidity == 0.5
    assert dna.temperature == 0.4
    assert dna.erosion == 0.3
    assert dna.water_level == 0.2
    assert dna.stability == 0.9


def test_planet_dna_is_immutable() -> None:
    dna = PlanetDNA(
        continentality=0.8,
        relief=0.7,
        volcanism=0.6,
        humidity=0.5,
        temperature=0.4,
        erosion=0.3,
        water_level=0.2,
        stability=0.9,
    )

    with pytest.raises(AttributeError):
        dna.relief = 0.1