from engine.terrain.world_map import WorldMap
from engine.visualization.solar_visualizer import SolarRadiationVisualizer
from engine.visualization.temperature_visualizer import TemperatureVisualizer


class AuroraObservatory:
    """
    Centralizes the scientific visualizations of the SEED Engine.
    """

    def __init__(self) -> None:
        self.solar = SolarRadiationVisualizer()
        self.temperature = TemperatureVisualizer()

    def render(
        self,
        world_map: WorldMap,
    ) -> str:
        sections: list[str] = []

        sections.append("=" * 40)
        sections.append("AURORA OBSERVATORY")
        sections.append("=" * 40)
        sections.append("")

        sections.append("SOLAR RADIATION")
        sections.append("")
        sections.append(
            self.solar.render(world_map)
        )

        sections.append("")
        sections.append("-" * 40)
        sections.append("")

        sections.append("TEMPERATURE")
        sections.append("")
        sections.append(
            self.temperature.render(world_map)
        )

        sections.append("")
        sections.append("=" * 40)

        return "\n".join(sections)