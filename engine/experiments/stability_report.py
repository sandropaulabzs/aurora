from dataclasses import dataclass

from engine.experiments.stability_snapshot import (
    StabilitySnapshot,
)


@dataclass(slots=True, frozen=True)
class StabilityReport:
    """
    Result of a long-running planetary stability experiment.
    """

    snapshots: tuple[
        StabilitySnapshot,
        ...,
    ]