from engine.terrain.world_map import WorldMap
from engine.visualization.surface_water_visualizer import (
    SurfaceWaterVisualizer,
)


def test_surface_water_visualizer_converts_values_to_symbols() -> None:
    world_map = WorldMap(width=3, height=1)

    dry = world_map.get_tile(0, 0)
    medium = world_map.get_tile(1, 0)
    flooded = world_map.get_tile(2, 0)

    assert dry is not None
    assert medium is not None
    assert flooded is not None

    dry.surface_water = 0.0
    medium.surface_water = 0.5
    flooded.surface_water = 1.0

    result = SurfaceWaterVisualizer().render(world_map)

    assert result == " =@"