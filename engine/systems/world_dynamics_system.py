from engine.atmosphere.condensation import CondensationModel
from engine.atmosphere.precipitation_threshold import (
    PrecipitationThresholdModel,
)
from engine.atmosphere.pressure import PressureModel
from engine.atmosphere.solar_radiation import SolarRadiation
from engine.atmosphere.temperature import TemperatureModel
from engine.atmosphere.vapor_capacity import VaporCapacityModel
from engine.atmosphere.wind_field import WindField
from engine.core.world import World
from engine.hydrology.evaporation import EvaporationModel
from engine.hydrology.evaporation_transfer import EvaporationTransfer
from engine.hydrology.moisture_transport import MoistureTransport
from engine.hydrology.precipitation import PrecipitationModel
from engine.systems.system import System


class WorldDynamicsSystem(System):
    """
    Executes the continuous natural processes of the world.

    These processes belong to evolution, not genesis.
    """

    def __init__(self, world: World) -> None:
        self.world = world

        self.solar_radiation = SolarRadiation()
        self.temperature_model = TemperatureModel()
        self.vapor_capacity_model = VaporCapacityModel()
        self.precipitation_threshold_model = (
            PrecipitationThresholdModel()
        )
        self.pressure_model = PressureModel()
        self.wind_field = WindField()

        self.evaporation_model = EvaporationModel()
        self.evaporation_transfer = EvaporationTransfer()
        self.moisture_transport = MoistureTransport()
        self.condensation_model = CondensationModel()
        self.precipitation_model = PrecipitationModel()

    def update(self) -> None:
        self.solar_radiation.apply(
            self.world.map,
        )

        self.temperature_model.apply(
            world_map=self.world.map,
            atmosphere=self.world.atmosphere,
        )

        self.vapor_capacity_model.apply(
            self.world.map,
        )

        self.precipitation_threshold_model.apply(
            self.world.map,
        )

        self.pressure_model.apply(
            world_map=self.world.map,
            atmosphere=self.world.atmosphere,
        )

        self.wind_field.apply(
            self.world.map,
        )

        self.evaporation_model.apply(
            self.world.map,
        )

        self.evaporation_transfer.apply(
            world_map=self.world.map,
            transfer_rate=0.05,
        )

        self.moisture_transport.apply(
            world_map=self.world.map,
            transport_rate=0.10,
        )

        self.condensation_model.apply(
            self.world.map,
        )

        self.precipitation_model.apply(
            self.world.map,
        )