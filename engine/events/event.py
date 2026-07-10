from dataclasses import dataclass, field
from datetime import datetime, UTC
import uuid


@dataclass(slots=True, frozen=True, kw_only=True)
class Event:
    """
    Classe base para todos os eventos da SEED Engine.
    """

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )