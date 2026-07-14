from engine.terrain.world_map import WorldMap
from engine.visualization.wind_visualizer import WindVisualizer


def test_wind_visualizer_renders_direction_symbols() -> None:
    world_map = WorldMap(width=3, height=1)

    calm = world_map.get_tile(0, 0)
    east = world_map.get_tile(1, 0)
    northwest = world_map.get_tile(2, 0)

    assert calm is not None
    assert east is not None
    assert northwest is not None

    calm.wind_dx = 0
    calm.wind_dy = 0

    east.wind_dx = 1
    east.wind_dy = 0

    northwest.wind_dx = -1
    northwest.wind_dy = -1

    visualizer = WindVisualizer()

    result = visualizer.render(world_map)

    assert result == "·→↖"


def test_wind_visualizer_marks_invalid_direction() -> None:
    world_map = WorldMap(width=1, height=1)

    tile = world_map.get_tile(0, 0)

    assert tile is not None

    tile.wind_dx = 2
    tile.wind_dy = 0

    result = WindVisualizer().render(world_map)

    assert result == "?"