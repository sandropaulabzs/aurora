from engine.core.world import World
from engine.experiments.experiment_result_formatter import (
    ExperimentResultFormatter,
)
from engine.experiments.experiment_runner import (
    ExperimentRunner,
)


class ExperimentConsole:
    """
    Executes an Aurora experiment and returns
    its formatted scientific result.
    """

    def __init__(self) -> None:
        self.runner = ExperimentRunner()
        self.formatter = ExperimentResultFormatter()

    def run(
        self,
        world: World,
        ticks: int,
    ) -> str:
        result = self.runner.run(
            world=world,
            ticks=ticks,
        )

        return self.formatter.format(
            result,
        )