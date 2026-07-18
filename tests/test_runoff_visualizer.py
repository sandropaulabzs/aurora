from engine.terrain.world_map import WorldMap
from engine.visualization.runoff_visualizer import (
    RunoffVisualizer,
)


def test_runoff_visualizer_converts_values_to_symbols() -> None:
    world_map = WorldMap(width=3, height=1)

    none = world_map.get_tile(0, 0)
    medium = world_map.get_tile(1, 0)
    strong = world_map.get_tile(2, 0)

    assert none is not None
    assert medium is not None
    assert strong is not None

    none.runoff = 0.0
    medium.runoff = 0.5
    strong.runoff = 1.0

    result = RunoffVisualizer().render(
        world_map
    )

    assert result == " =@"