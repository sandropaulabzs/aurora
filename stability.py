from engine.core.world import World
from engine.experiments.stability_console import (
    StabilityConsole,
)
from engine.terrain.world_seed import WorldSeed


def main() -> None:
    world = World(
        name="Aurora Stability World",
        width=32,
        height=32,
        seed=WorldSeed(24680),
    )

    world.initialize()

    report = StabilityConsole().run(
        world=world,
        ticks=10000,
        snapshot_interval=1000,
    )

    print()
    print(report)
    print()


if __name__ == "__main__":
    main()