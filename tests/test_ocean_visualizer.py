from engine.terrain.world_map import WorldMap
from engine.visualization.ocean_visualizer import (
    OceanVisualizer,
)


def test_ocean_visualizer_distinguishes_land_and_ocean() -> None:
    world_map = WorldMap(width=3, height=1)

    land = world_map.get_tile(0, 0)
    ocean = world_map.get_tile(1, 0)
    land_again = world_map.get_tile(2, 0)

    assert land is not None
    assert ocean is not None
    assert land_again is not None

    land.is_ocean = False
    ocean.is_ocean = True
    land_again.is_ocean = False

    result = OceanVisualizer().render(
        world_map
    )

    assert result == " ~ "


def test_empty_world_map_renders_empty_string() -> None:
    world_map = WorldMap(width=0, height=0)

    result = OceanVisualizer().render(
        world_map
    )

    assert result == ""