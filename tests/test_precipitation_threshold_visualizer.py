from engine.terrain.world_map import WorldMap
from engine.visualization.precipitation_threshold_visualizer import (
    PrecipitationThresholdVisualizer,
)


def test_precipitation_threshold_visualizer_converts_values_to_symbols() -> None:
    world_map = WorldMap(width=3, height=1)

    low = world_map.get_tile(0, 0)
    medium = world_map.get_tile(1, 0)
    high = world_map.get_tile(2, 0)

    assert low is not None
    assert medium is not None
    assert high is not None

    low.precipitation_threshold = 0.20
    medium.precipitation_threshold = 0.45
    high.precipitation_threshold = 0.70

    result = PrecipitationThresholdVisualizer().render(
        world_map
    )

    assert result == " =@"