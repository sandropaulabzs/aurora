from engine.core.world import World
from engine.hydrology.runoff import RunoffModel
from engine.hydrology.water_passage import WaterPassageModel
from engine.hydrology.water_passage_decay import (
    WaterPassageDecayModel,
)
from engine.terrain.world_seed import WorldSeed


def test_repeated_runoff_builds_persistent_water_passage() -> None:
    world = World(
        width=3,
        height=1,
        seed=WorldSeed(12345),
    )

    world.initialize()

    high = world.map.get_tile(0, 0)
    middle = world.map.get_tile(1, 0)
    low = world.map.get_tile(2, 0)

    assert high is not None
    assert middle is not None
    assert low is not None

    high.altitude = 1.0
    middle.altitude = 0.5
    low.altitude = 0.0

    high.surface_water = 1.0

    runoff = RunoffModel()
    decay = WaterPassageDecayModel()
    passage = WaterPassageModel()

    for _ in range(20):
        runoff.apply(
            world.map,
            runoff_rate=0.10,
        )

        decay.apply(
            world.map,
            decay=0.9999,
        )

        passage.apply(
            world.map,
        )

    assert high.water_passage > 0.0
    assert middle.water_passage > 0.0

    assert (
        high.water_passage
        >
        middle.water_passage
    )