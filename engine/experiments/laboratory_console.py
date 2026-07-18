from engine.core.world import World
from engine.experiments.aurora_laboratory import (
    AuroraLaboratory,
)
from engine.experiments.laboratory_result_formatter import (
    LaboratoryResultFormatter,
)


class LaboratoryConsole:
    """
    Executes an Aurora laboratory experiment
    and returns a formatted scientific report.
    """

    def __init__(self) -> None:
        self.laboratory = AuroraLaboratory()
        self.formatter = (
            LaboratoryResultFormatter()
        )

    def run(
        self,
        world: World,
        ticks: int,
    ) -> str:
        result = self.laboratory.run(
            world=world,
            ticks=ticks,
        )

        return self.formatter.format(
            result,
        )