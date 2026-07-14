from engine.terrain.world_map import WorldMap
from engine.visualization.cloud_water_visualizer import (
    CloudWaterVisualizer,
)


def test_cloud_water_visualizer_converts_values_to_symbols() -> None:
    world_map = WorldMap(width=3, height=1)

    clear = world_map.get_tile(0, 0)
    medium = world_map.get_tile(1, 0)
    dense = world_map.get_tile(2, 0)

    assert clear is not None
    assert medium is not None
    assert dense is not None

    clear.cloud_water = 0.0
    medium.cloud_water = 0.5
    dense.cloud_water = 1.0

    result = CloudWaterVisualizer().render(world_map)

    assert result == " =@"