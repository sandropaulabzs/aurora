from engine.terrain.ocean import is_ocean
from engine.terrain.sea_level import SeaLevel
from engine.terrain.tile import Tile


def test_tile_below_sea_level_is_ocean() -> None:
    tile = Tile(
        x=0,
        y=0,
        altitude=0.25,
    )

    sea_level = SeaLevel(0.40)

    assert is_ocean(tile, sea_level) is True


def test_tile_at_sea_level_is_ocean() -> None:
    tile = Tile(
        x=0,
        y=0,
        altitude=0.40,
    )

    sea_level = SeaLevel(0.40)

    assert is_ocean(tile, sea_level) is True


def test_tile_above_sea_level_is_land() -> None:
    tile = Tile(
        x=0,
        y=0,
        altitude=0.75,
    )

    sea_level = SeaLevel(0.40)

    assert is_ocean(tile, sea_level) is False