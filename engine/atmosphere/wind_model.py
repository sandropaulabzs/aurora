from engine.atmosphere.pressure_flow import (
    find_lowest_pressure_neighbor,
)
from engine.atmosphere.pressure_gradient import (
    calculate_pressure_gradient,
)
from engine.atmosphere.wind import WindVector
from engine.terrain.tile import Tile
from engine.terrain.world_map import WorldMap


class WindModel:
    """
    Calculates local wind from atmospheric pressure differences.
    """

    def calculate(
        self,
        world_map: WorldMap,
        origin: Tile,
    ) -> WindVector:
        target = find_lowest_pressure_neighbor(
            world_map,
            origin,
        )

        pressure_gradient = calculate_pressure_gradient(
            origin,
            target,
        )

        if pressure_gradient <= 0.0:
            return WindVector(
                dx=0,
                dy=0,
                speed=0.0,
            )

        dx = target.x - origin.x
        dy = target.y - origin.y

        speed = max(
            0.0,
            min(pressure_gradient, 1.0),
        )

        return WindVector(
            dx=dx,
            dy=dy,
            speed=speed,
        )