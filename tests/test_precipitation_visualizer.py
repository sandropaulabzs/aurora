from engine.terrain.world_map import WorldMap
from engine.visualization.precipitation_visualizer import (
    PrecipitationVisualizer,
)


def test_precipitation_visualizer_normalizes_current_tick_values() -> None:
    world_map = WorldMap(width=3, height=1)

    none = world_map.get_tile(0, 0)
    medium = world_map.get_tile(1, 0)
    maximum = world_map.get_tile(2, 0)

    assert none is not None
    assert medium is not None
    assert maximum is not None

    none.precipitation = 0.0
    medium.precipitation = 0.5
    maximum.precipitation = 1.0

    result = PrecipitationVisualizer().render(
        world_map
    )

    assert result == " =@"


def test_positive_precipitation_trace_is_always_visible() -> None:
    world_map = WorldMap(width=2, height=1)

    faint = world_map.get_tile(0, 0)
    maximum = world_map.get_tile(1, 0)

    assert faint is not None
    assert maximum is not None

    faint.precipitation = 0.0001
    maximum.precipitation = 100.0

    result = PrecipitationVisualizer().render(
        world_map
    )

    assert result[0] == "."
    assert result[1] == "@"


def test_empty_world_map_renders_empty_string() -> None:
    world_map = WorldMap(width=0, height=0)

    result = PrecipitationVisualizer().render(
        world_map
    )

    assert result == ""