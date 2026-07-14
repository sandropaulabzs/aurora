from engine.terrain.world_map import WorldMap


class WindVisualizer:
    """
    Renders the local wind field using directional ASCII symbols.
    """

    DIRECTION_SYMBOLS: dict[tuple[int, int], str] = {
        (0, 0): "·",
        (0, -1): "↑",
        (1, -1): "↗",
        (1, 0): "→",
        (1, 1): "↘",
        (0, 1): "↓",
        (-1, 1): "↙",
        (-1, 0): "←",
        (-1, -1): "↖",
    }

    def render(self, world_map: WorldMap) -> str:
        lines: list[str] = []

        for y in range(world_map.height):
            row: list[str] = []

            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                direction = (
                    tile.wind_dx,
                    tile.wind_dy,
                )

                row.append(
                    self.DIRECTION_SYMBOLS.get(
                        direction,
                        "?",
                    )
                )

            lines.append("".join(row))

        return "\n".join(lines)