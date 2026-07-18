from engine.analysis.world_analyzer import WorldAnalyzer
from engine.analysis.world_report_formatter import (
    WorldReportFormatter,
)
from engine.core.world import World


class ObservatoryConsole:
    """
    Presents scientific observations about the world.
    """

    def __init__(self) -> None:
        self.analyzer = WorldAnalyzer()
        self.formatter = WorldReportFormatter()

    def render(
        self,
        world: World,
    ) -> str:
        report = self.analyzer.analyze(
            world.map,
        )

        return self.formatter.format(
            report,
        )