from engine.terrain.world_map import WorldMap
from engine.visualization.atmospheric_moisture_visualizer import (
    AtmosphericMoistureVisualizer,
)
from engine.visualization.cloud_water_visualizer import (
    CloudWaterVisualizer,
)
from engine.visualization.ocean_visualizer import OceanVisualizer
from engine.visualization.precipitation_threshold_visualizer import (
    PrecipitationThresholdVisualizer,
)
from engine.visualization.pressure_visualizer import PressureVisualizer
from engine.visualization.runoff_visualizer import RunoffVisualizer
from engine.visualization.solar_visualizer import (
    SolarRadiationVisualizer,
)
from engine.visualization.surface_water_visualizer import (
    SurfaceWaterVisualizer,
)
from engine.visualization.temperature_visualizer import (
    TemperatureVisualizer,
)
from engine.visualization.vapor_capacity_visualizer import (
    VaporCapacityVisualizer,
)
from engine.visualization.water_passage_visualizer import (
    WaterPassageVisualizer,
)
from engine.visualization.wind_visualizer import WindVisualizer


class AuroraObservatory:
    """
    Centralizes the scientific visualizations of the SEED Engine.
    """

    def __init__(self) -> None:
        self.ocean = OceanVisualizer()

        self.solar = SolarRadiationVisualizer()
        self.temperature = TemperatureVisualizer()
        self.pressure = PressureVisualizer()
        self.wind = WindVisualizer()

        self.atmospheric_moisture = (
            AtmosphericMoistureVisualizer()
        )
        self.vapor_capacity = VaporCapacityVisualizer()
        self.cloud_water = CloudWaterVisualizer()
        self.precipitation_threshold = (
            PrecipitationThresholdVisualizer()
        )

        self.surface_water = SurfaceWaterVisualizer()
        self.runoff = RunoffVisualizer()
        self.water_passage = WaterPassageVisualizer()

    def render(
        self,
        world_map: WorldMap,
    ) -> str:
        sections: list[str] = []

        sections.append("=" * 40)
        sections.append("AURORA OBSERVATORY")
        sections.append("=" * 40)
        sections.append("")

        sections.append("OCEAN MASK")
        sections.append("")
        sections.append(
            self.ocean.render(world_map)
        )

        sections.append("")
        sections.append("-" * 40)
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
        sections.append("-" * 40)
        sections.append("")

        sections.append("ATMOSPHERIC PRESSURE")
        sections.append("")
        sections.append(
            self.pressure.render(world_map)
        )

        sections.append("")
        sections.append("-" * 40)
        sections.append("")

        sections.append("WIND DIRECTION")
        sections.append("")
        sections.append(
            self.wind.render(world_map)
        )

        sections.append("")
        sections.append("-" * 40)
        sections.append("")

        sections.append("ATMOSPHERIC MOISTURE")
        sections.append("")
        sections.append(
            self.atmospheric_moisture.render(
                world_map
            )
        )

        sections.append("")
        sections.append("-" * 40)
        sections.append("")

        sections.append("VAPOR CAPACITY")
        sections.append("")
        sections.append(
            self.vapor_capacity.render(world_map)
        )

        sections.append("")
        sections.append("-" * 40)
        sections.append("")

        sections.append("CLOUD WATER")
        sections.append("")
        sections.append(
            self.cloud_water.render(world_map)
        )

        sections.append("")
        sections.append("-" * 40)
        sections.append("")

        sections.append("PRECIPITATION THRESHOLD")
        sections.append("")
        sections.append(
            self.precipitation_threshold.render(
                world_map
            )
        )

        sections.append("")
        sections.append("-" * 40)
        sections.append("")

        sections.append("SURFACE WATER")
        sections.append("")
        sections.append(
            self.surface_water.render(world_map)
        )

        sections.append("")
        sections.append("-" * 40)
        sections.append("")

        sections.append("RUNOFF")
        sections.append("")
        sections.append(
            self.runoff.render(world_map)
        )

        sections.append("")
        sections.append("-" * 40)
        sections.append("")

        sections.append("WATER PASSAGE MEMORY")
        sections.append("")
        sections.append(
            self.water_passage.render(world_map)
        )

        sections.append("")
        sections.append("=" * 40)

        return "\n".join(sections)