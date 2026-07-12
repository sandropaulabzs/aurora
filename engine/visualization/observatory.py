from engine.terrain.world_map import WorldMap
from engine.visualization.solar_visualizer import SolarRadiationVisualizer


class AuroraObservatory:
    """
    Centraliza todas as visualizações científicas da Engine.
    """

    def __init__(self) -> None:
        self.solar = SolarRadiationVisualizer()

    def render(
        self,
        world_map: WorldMap,
    ) -> str:

        sections = []

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
        sections.append("=" * 40)

        return "\n".join(sections)