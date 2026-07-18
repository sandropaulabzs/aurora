from engine.terrain.world_map import WorldMap
from engine.visualization.water_passage_visualizer import (
    WaterPassageVisualizer,
)


def test_water_passage_visualizer_normalizes_against_maximum() -> None:
    world_map = WorldMap(width=3, height=1)

    none = world_map.get_tile(0, 0)
    medium = world_map.get_tile(1, 0)
    maximum = world_map.get_tile(2, 0)

    assert none is not None
    assert medium is not None
    assert maximum is not None

    none.water_passage = 0.0
    medium.water_passage = 5.0
    maximum.water_passage = 10.0

    result = WaterPassageVisualizer().render(
        world_map
    )

    assert result == " =@"


def test_positive_trace_is_always_visible() -> None:
    world_map = WorldMap(width=2, height=1)

    faint = world_map.get_tile(0, 0)
    maximum = world_map.get_tile(1, 0)

    assert faint is not None
    assert maximum is not None

    faint.water_passage = 0.0001
    maximum.water_passage = 100.0

    result = WaterPassageVisualizer().render(
        world_map
    )

    assert result[0] == "."
    assert result[1] == "@"


def test_empty_world_map_renders_empty_string() -> None:
    world_map = WorldMap(width=0, height=0)

    result = WaterPassageVisualizer().render(
        world_map
    )

    assert result == ""