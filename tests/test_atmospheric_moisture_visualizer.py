from engine.terrain.world_map import WorldMap
from engine.visualization.atmospheric_moisture_visualizer import (
    AtmosphericMoistureVisualizer,
)


def test_atmospheric_moisture_visualizer_converts_values_to_symbols() -> None:
    world_map = WorldMap(width=3, height=1)

    dry = world_map.get_tile(0, 0)
    medium = world_map.get_tile(1, 0)
    saturated = world_map.get_tile(2, 0)

    assert dry is not None
    assert medium is not None
    assert saturated is not None

    dry.atmospheric_moisture = 0.0
    medium.atmospheric_moisture = 0.5
    saturated.atmospheric_moisture = 1.0

    result = AtmosphericMoistureVisualizer().render(world_map)

    assert result == " =@"