from engine.terrain.world_map import WorldMap
from engine.visualization.vapor_capacity_visualizer import (
    VaporCapacityVisualizer,
)


def test_vapor_capacity_visualizer_converts_values_to_symbols() -> None:
    world_map = WorldMap(width=3, height=1)

    low = world_map.get_tile(0, 0)
    medium = world_map.get_tile(1, 0)
    high = world_map.get_tile(2, 0)

    assert low is not None
    assert medium is not None
    assert high is not None

    low.vapor_capacity = 0.0
    medium.vapor_capacity = 0.5
    high.vapor_capacity = 1.0

    result = VaporCapacityVisualizer().render(world_map)

    assert result == " =@"