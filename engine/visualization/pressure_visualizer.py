from engine.terrain.world_map import WorldMap


class PressureVisualizer:
    """
    Renders the atmospheric pressure layer in ASCII.
    """

    SYMBOLS = " .:-=+*#%@"

    def render(self, world_map: WorldMap) -> str:
        lines: list[str] = []

        max_index = len(self.SYMBOLS) - 1

        for y in range(world_map.height):
            row: list[str] = []

            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                pressure = max(
                    0.0,
                    min(tile.pressure, 1.0),
                )

                index = int(
                    pressure * max_index
                )

                row.append(
                    self.SYMBOLS[index]
                )

            lines.append(
                "".join(row)
            )

        return "\n".join(lines)