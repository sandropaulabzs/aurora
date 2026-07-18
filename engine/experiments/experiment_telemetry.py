from dataclasses import dataclass


@dataclass(slots=True)
class ExperimentTelemetry:
    """
    Tracks the highest hydrological values observed
    during an experiment.

    These values describe the history of the simulation,
    rather than only its final state.
    """

    maximum_cloud_water: float = 0.0
    maximum_precipitation: float = 0.0
    maximum_surface_water: float = 0.0
    maximum_infiltration: float = 0.0
    maximum_runoff: float = 0.0
    maximum_water_passage: float = 0.0

    maximum_precipitating_tiles: int = 0