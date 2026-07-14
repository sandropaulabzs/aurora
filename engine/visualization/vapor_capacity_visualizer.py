from engine.terrain.world_map import WorldMap


class VaporCapacityVisualizer:
    """
    Renders atmospheric vapor capacity in ASCII.
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

                capacity = max(
                    0.0,
                    min(tile.vapor_capacity, 1.0),
                )

                index = int(
                    capacity * max_index
                )

                row.append(self.SYMBOLS[index])

            lines.append("".join(row))

        return "\n".join(lines)