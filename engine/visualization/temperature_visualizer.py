from engine.terrain.world_map import WorldMap


class TemperatureVisualizer:
    """
    Renders the planet's temperature layer in ASCII.
    """

    SYMBOLS = " .:-=+*#%@"

    MIN_TEMPERATURE = -30.0
    MAX_TEMPERATURE = 50.0

    def render(self, world_map: WorldMap) -> str:
        lines: list[str] = []
        max_index = len(self.SYMBOLS) - 1

        temperature_range = (
            self.MAX_TEMPERATURE
            - self.MIN_TEMPERATURE
        )

        for y in range(world_map.height):
            row: list[str] = []

            for x in range(world_map.width):
                tile = world_map.get_tile(x, y)

                assert tile is not None

                normalized_temperature = (
                    tile.temperature
                    - self.MIN_TEMPERATURE
                ) / temperature_range

                normalized_temperature = max(
                    0.0,
                    min(normalized_temperature, 1.0),
                )

                index = int(
                    normalized_temperature * max_index
                )

                row.append(self.SYMBOLS[index])

            lines.append("".join(row))

        return "\n".join(lines)