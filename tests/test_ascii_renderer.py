from engine.rendering.ascii_renderer import AsciiRenderer
from engine.terrain.world_map import WorldMap


def test_ascii_renderer_converts_altitude_to_symbols() -> None:
    world_map = WorldMap(width=3, height=1)

    first_tile = world_map.get_tile(0, 0)
    second_tile = world_map.get_tile(1, 0)
    third_tile = world_map.get_tile(2, 0)

    assert first_tile is not None
    assert second_tile is not None
    assert third_tile is not None

    first_tile.altitude = 0.0
    second_tile.altitude = 0.5
    third_tile.altitude = 1.0

    renderer = AsciiRenderer()

    result = renderer.render(world_map)

    assert result == " =@"