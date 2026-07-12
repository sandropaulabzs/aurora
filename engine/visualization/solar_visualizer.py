from engine.terrain.world_map import WorldMap


class SolarRadiationVisualizer:
    """
    Renders the planet's solar radiation layer in ASCII.
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

                light = max(
                    0.0,
                    min(tile.light, 1.0),
                )

                index = int(light * max_index)
                row.append(self.SYMBOLS[index])

            lines.append("".join(row))

        return "\n".join(lines)