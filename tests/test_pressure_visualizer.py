from engine.terrain.world_map import WorldMap
from engine.visualization.pressure_visualizer import PressureVisualizer


def test_pressure_visualizer_converts_pressure_to_symbols() -> None:
    world_map = WorldMap(width=3, height=1)

    low = world_map.get_tile(0, 0)
    medium = world_map.get_tile(1, 0)
    high = world_map.get_tile(2, 0)

    assert low is not None
    assert medium is not None
    assert high is not None

    low.pressure = 0.0
    medium.pressure = 0.5
    high.pressure = 1.0

    visualizer = PressureVisualizer()

    result = visualizer.render(world_map)

    assert result == " =@"